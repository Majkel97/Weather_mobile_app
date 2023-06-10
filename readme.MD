# Mobile Weather App - Dokumentacja techniczna

## Spis treści

1.  [Instalacja](#instalacja)
2.  [Uruchomienie aplikacji](#uruchomienie-aplikacji)
3.  [Utworzenie pakietu instalacyjnego dla środowiska Android](#utworzenie-pakietu-instalacyjnego-dla-środowiska-android)

## Instalacja

1. Pobierz repozytorium z kodem i otwórz folder z projektem przy użyciu dowolnego IDE (na przykład Visual Stuido Code).

2. Utwórz wirtualne środowisko i aktywuj je.

```bash
# Utworzenie środkowiska wirtualnego
python -m venv /path/to/new/virtual/environment
# Aktywacja środkowiska wirtualnego
.\env\Scripts\activate
```

3. Używając menedżera pakietów [pip](https://pip.pypa.io/en/stable/), zainstaluj wymagane biblioteki.

```bash
pip install -r requirements.txt
```

## Uruchomienie aplikacji

1. Utwórz konto oraz idywiduakny klucz API na portalu [Open Weather Map](https://openweathermap.org/)
2. Wrowadź Twój klucz API w pliku `main.py`

```python
# Replace API_KEY with your OpenWeatherMap API key
API_KEY = 'YOUR_OPEN_WEATHER_MAP_API_KEY'
```

3. Uruchom aplikację używając poniższego polecenia (pamiętaj o aktywacji środowiska wirtualnego opisanego w sekcji wyżej):

```bash
python3 main.py
```

## Utworzenie pakietu instalacyjnego dla środowiska Android

1. Aby utworzyć aplikację gotową do uruchomienia w środowisku Android, należy przygotować pakiet instalacyjny z rozszerzeniem `.apk`, który będzie można uruchomić na urządzeniu mobilnym.
2. Aby stworzyć pakiet instalacyjny, możemy wykorzystać system operacyjny Windows oraz narzędzie [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb) lub system operacyjny Linux.
3. W wybranym systemie należy uruchomić poniższe polecenia:

```bash
!pip install buildozer
```

```bash
!pip install cython==0.29.19
```

```bash
!sudo apt-get install -y \ python3-pip \ build-essential \ git \ python3 \ python3-dev \ ffmpeg \ libsdl2-dev \ libsdl2-image-dev \ libsdl2-mixer-dev \ libsdl2-ttf-dev \ libportmidi-dev \ libswscale-dev \ libavformat-dev \ libavcodec-dev \ zlib1g-dev
```

```bash
!sudo apt-get install -y \ libgstreamer1.0 \ gstreamer1.0-plugins-base \ gstreamer1.0-plugins-good
```

```bash
!sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev libffi6
```

```bash
!sudo apt-get install libffi-dev
```

```bash
!buildozer init
```

4. Po wykonaniu ostatniego polecenia zostanie utworzony plik `buildozer.spec`. Przed przystąpieniem do kolejnego kroku należy edytować utworzony plik, aby nadać tytuł aplikacji, określić wymagane pakiety z konkretnymi wersjami oraz wskazać potrzebne uprawnienia.

```python
# Title of your application
title = Weather App
...
# Application requirements
# Comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy
...
# Permissions
android.permissions = android.permission.INTERNET, (name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18)
```

5. Jako ostatni krok należy użyć komendy wskazanej poniżej.
   (UWAGA! Proces jest czasochłonny - może trwać nawet ponad 30 min w przypadku komputera ze słabymi podzespołami)

```bash
!buildozer -v android debug
```
