import requests
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel

MAX_FAVORITES = 5
API_KEY = "ae27d7f299bdcecf3944226af304831d"

KV = """
MDFloatLayout:
    md_bg_color: 1,1,1,1
    orientation: "vertical"

    MDLabel:
        id: content
        pos_hint: {"center_x": .5, "center_y": .6}
        text: "Search weather for your city..."
        font_size: "20sp"
        halign: "center"

    MDTopAppBar:
        id: toolbar
        title: "Weather App"
        right_action_items: [["magnify", lambda x: app.open_search()],["star", lambda x: app.fav_menu()]]
    
    Image:
        id: source
        source: ""
        size_hint: .1, .1
        pos_hint: {"center_x": .5, "center_y": 0.9}

    MDLabel:
        id: location
        pos_hint: {"center_x": .5, "center_y": .81}
        text: ""
        font_size: "20sp"
        halign: "center"

    Image:
        id: weather_type_img
        size_hint: .2, .2
        source: ""
        pos_hint: {"center_x": .5, "center_y": .73}

    MDLabel:
        id: temperature
        pos_hint: {"center_x": .5, "center_y": .62}
        text: ""
        font_size: "40sp"
        halign: "center"    

    MDLabel:
        id: weather_type_text
        pos_hint: {"center_x": .5, "center_y": .55}
        text: ""
        font_size: "20sp"
        halign: "center"

    Image:
        id: humidity_img
        size_hint: .1, .1
        source: ""
        pos_hint: {"center_x": .2, "center_y": .46}

    MDLabel:
        id: humidity
        pos_hint: {"center_x": .2, "center_y": .40}
        text: ""
        font_size: "18sp"
        halign: "center"

    Image:
        id: wind_img
        size_hint: .1, .1
        source: ""
        pos_hint: {"center_x": .50, "center_y": .46}

    MDLabel:
        id: wind
        pos_hint: {"center_x": .50, "center_y": .40}
        text: ""
        font_size: "18sp"
        halign: "center"

    Image:
        id: pressure_img
        size_hint: .1, .1
        source: ""
        pos_hint: {"center_x": .80, "center_y": .46}

    MDLabel:
        id: pressure
        pos_hint: {"center_x": .80, "center_y": .40}
        text: ""
        font_size: "18sp"
        halign: "center"

    Image:
        id: weather_day_1
        size_hint: .1, .1
        source: ""
        pos_hint: {"center_x": .2, "center_y": .30}

    MDLabel:
        id: temp_day_1
        pos_hint: {"center_x": .2, "center_y": .24}
        text: ""
        font_size: "18sp"
        halign: "center"
    
    MDLabel:
        id: date_day_1
        pos_hint: {"center_x": .2, "center_y": .15}
        text: ""
        font_size: "15sp"
        halign: "center"

    MDLabel:
        id: time_day_1
        pos_hint: {"center_x": .2, "center_y": .19}
        text: ""
        font_size: "15sp"
        halign: "center"

    Image:
        id: weather_day_2
        size_hint: .1, .1
        source: ""
        pos_hint: {"center_x": .50, "center_y": .30}

    MDLabel:
        id: temp_day_2
        pos_hint: {"center_x": .50, "center_y": .24}
        text: ""
        font_size: "18sp"
        halign: "center"

    MDLabel:
        id: date_day_2
        pos_hint: {"center_x": .50, "center_y": .15}
        text: ""
        font_size: "15sp"
        halign: "center"

    MDLabel:
        id: time_day_2
        pos_hint: {"center_x": .50, "center_y": .19}
        text: ""
        font_size: "15sp"
        halign: "center"

    Image:
        id: weather_day_3
        size_hint: .1, .1
        source: ""
        pos_hint: {"center_x": .80, "center_y": .30}

    MDLabel:
        id: temp_day_3
        pos_hint: {"center_x": .80, "center_y": .24}
        text: ""
        font_size: "18sp"
        halign: "center"

    MDLabel:
        id: date_day_3
        pos_hint: {"center_x": .80, "center_y": .15}
        text: ""
        font_size: "15sp"
        halign: "center"

    MDLabel:
        id: time_day_3
        pos_hint: {"center_x": .80, "center_y": .19}
        text: ""
        font_size: "15sp"
        halign: "center"

<MenuHeader>
    orientation: "vertical"
    adaptive_size: True
    padding: "4dp"

    MDBoxLayout:
        spacing: "12dp"
        adaptive_size: True

        MDIconButton:
            icon: "star"
            pos_hint: {"center_y": .5}

        MDLabel:
            text: "Click to select:"
            adaptive_size: True
            pos_hint: {"center_y": .5}

<MenuHeaderDel>
    orientation: "vertical"
    adaptive_size: True
    padding: "4dp"

    MDBoxLayout:
        spacing: "12dp"
        adaptive_size: True

        MDIconButton:
            icon: "bin"
            pos_hint: {"center_y": .5}

        MDLabel:
            text: "Click to delete:"
            adaptive_size: True
            pos_hint: {"center_y": .5}
"""


class MenuHeader(MDBoxLayout):
    """
    An instance of the class that will be added to the menu header.
    """


class MenuHeaderDel(MDBoxLayout):
    """
    An instance of the class that will be added to the menu header.
    """


class WeatherApp(MDApp):
    """
    Main application class for the Weather app.
    """

    dialog = None

    def __init__(self, **kwargs):
        """Initializes the main app screen and favorite_cities list.

        Calls the superclass constructor first, passing any keyword arguments to it.
        It then loads the KV string into the screen object and sets self.favorite_cities to an empty list.
        Finally, it calls self.fetch_weather with the argument "Kraków" (although this line is commented out).
        """

        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        self.favorite_cities = []
        # self.fetch_weather("Kraków")

    def build(self):
        return self.screen

    def fav_menu(self):
        """
        Displays a dropdown menu with favorite cities. If selected, fetches weather data for that city.

        If self.favorite_cities is not empty, it populates the dropdown menu with each city as a menu item,
        where selecting it calls the fetch_weather method with the selected city as an argument and dismisses the menu.
        Otherwise, the menu only has one item saying "Add city to favorite!".

        """
        if self.favorite_cities:
            menu_items = [
                {
                    "text": f"{city}",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=city: (
                        self.fetch_weather(x),
                        self.favorite.dismiss(),
                    ),
                }
                for city in self.favorite_cities
            ]
        else:
            menu_items = [
                {
                    "text": f"Add city to favorite!",
                    "viewclass": "OneLineListItem",
                }
            ]
        self.favorite = MDDropdownMenu(
            header_cls=MenuHeader(),
            caller=self.screen.ids.toolbar,
            items=menu_items,
            width_mult=4,
        )
        self.favorite.open()

    def delete_fav_menu(self):
        """
        Opens a dropdown menu to display a list of favorite cities. Users can select a city from the list and remove it from their favorites.
        """
        if self.favorite_cities:
            menu_items = [
                {
                    "text": f"{city}",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=city: (
                        self.remove_from_favorites(x),
                        self.favorite_del.dismiss(),
                    ),
                }
                for city in self.favorite_cities
            ]

        self.favorite_del = MDDropdownMenu(
            header_cls=MenuHeaderDel(),
            caller=self.screen.ids.toolbar,
            items=menu_items,
            width_mult=4,
        )
        self.favorite_del.open()

    def remove_from_favorites(self, city_name):
        """
        Removes a city from the list of favorite cities.
        """

        if city_name in self.favorite_cities:
            self.favorite_cities.remove(city_name)

    def open_search(self):
        """
        Method to open dialog with 2 inputs (Text type for city name, and checkbox for True / False).
        Dialog have 2 buttons - Cancel to close dialog, Ok to show data
        """

        self.dialog = MDDialog(
            title="Search city:",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(
                    id="city",
                    hint_text="City",
                ),
                MDLabel(
                    text="Add to favorites?",
                    theme_text_color="Secondary",
                ),
                MDCheckbox(
                    id="fav_checkbox",
                ),
                orientation="vertical",
                spacing="12dp",
                size_hint_y=None,
                height="120dp",
            ),
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog,
                ),
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.search_city,
                ),
            ],
        )
        self.dialog.open()

    def close_dialog(self, obj):
        """
        Close opened dialog.
        """
        self.dialog.dismiss()

    def search_city(self, instance):
        """
        Fetches weather information for a specified city and optionally adds it to the list of favorite cities.
        """

        city_name = self.dialog.content_cls.ids.city.text
        self.fetch_weather(city_name)
        self.dialog.dismiss()
        if self.dialog.content_cls.ids.fav_checkbox.active:
            self.add_to_favorites(city_name)

    def add_to_favorites(self, city_name):
        """
        Adds a city to the list of favorite cities.
        """

        if len(self.favorite_cities) < MAX_FAVORITES:
            if city_name not in self.favorite_cities:
                self.favorite_cities.append(city_name)
        else:
            self.delete_fav_menu()

    def fetch_weather(self, city_name):
        """
        Fetches weather data for a given city and updates the user interface with the weather information, and add information to screen

        Args:
            city_name (str): The name of the city to fetch weather data for.

        API Reference:
            This method uses the OpenWeatherMap API to fetch weather data.
        """

        if city_name:
            weather = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
            forecast = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric&cnt=3"
            response_weather = requests.get(weather)
            data = response_weather.json()
            response_forecast = requests.get(forecast)
            data_forecast = response_forecast.json()

            if data.get("cod") != "404":
                self.screen.ids.location.text = (
                    f"{data['name']}, {data['sys']['country']}"
                )
                self.screen.ids.weather_type_img.source = (
                    f"img/{data['weather'][0]['icon']}@2x.png"
                )
                self.screen.ids.content.text = f""
                self.screen.ids.humidity_img.source = f"img/humidity.png"
                self.screen.ids.wind_img.source = f"img/wind.png"
                self.screen.ids.pressure_img.source = f"img/pressure.png"
                self.screen.ids.source.source = f"img/location.png"
                self.screen.ids.temperature.text = f"{data['main']['temp']}°C"
                self.screen.ids.weather_type_text.text = data["weather"][0]["main"]
                self.screen.ids.humidity.text = f"{data['main']['humidity']}%"
                self.screen.ids.wind.text = f"{data['wind']['speed']} m/s {self.wind_deg_to_directions(data['wind']['deg'])}"
                self.screen.ids.pressure.text = f"{data['main']['pressure']} hPa"

                for i in range(3):
                    forecast = data_forecast["list"][i]
                    weather_day = f"img/{forecast['weather'][0]['icon']}@2x.png"
                    temp_day = forecast["main"]["temp"]
                    date_day, time_day = forecast["dt_txt"].split(" ")
                    self.screen.ids[f"weather_day_{i+1}"].source = weather_day
                    self.screen.ids[f"temp_day_{i+1}"].text = f"{temp_day}°C"
                    self.screen.ids[f"date_day_{i+1}"].text = f"{date_day}"
                    self.screen.ids[f"time_day_{i+1}"].text = f"{time_day}"

            else:
                self.clear_screen()
                self.screen.ids.content.text = "City not found"
        else:
            self.clear_screen()
            self.screen.ids.content.text = "Please enter a city name"

    def clear_screen(self):
        """
        Clears the weather information displayed on the screen.
        """

        self.screen.ids.location.text = ""
        self.screen.ids.weather_type_img.source = ""
        self.screen.ids.content.text = ""
        self.screen.ids.humidity_img.source = ""
        self.screen.ids.wind_img.source = ""
        self.screen.ids.pressure_img.source = ""
        self.screen.ids.source.source = ""
        self.screen.ids.temperature.text = ""
        self.screen.ids.weather_type_text.text = ""
        self.screen.ids.humidity.text = ""
        self.screen.ids.wind.text = ""
        self.screen.ids.pressure.text = ""
        for i in range(3):
            self.screen.ids[f"weather_day_{i+1}"].source = ""
            self.screen.ids[f"temp_day_{i+1}"].text = ""
            self.screen.ids[f"date_day_{i+1}"].text = ""
            self.screen.ids[f"time_day_{i+1}"].text = ""

    def wind_deg_to_directions(self, deg):
        """
        Converts wind direction in degrees to cardinal directions.

        Parameters:
            deg (int or float): Wind direction in degrees.

        Returns:
            str: Cardinal direction corresponding to the input degree value.

        Example usage:
            >>> wind_deg_to_directions(90)
            "E"
        """
        directions = [
            "N",
            "NNE",
            "NE",
            "ENE",
            "E",
            "ESE",
            "SE",
            "SSE",
            "S",
            "SSW",
            "SW",
            "WSW",
            "W",
            "WNW",
            "NW",
            "NNW",
        ]
        direction = round(deg / 22.5) % 16
        return directions[direction]


if __name__ == "__main__":
    WeatherApp().run()
