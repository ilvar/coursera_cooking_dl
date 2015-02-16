# coursera cooking downloader

Downloader for https://www.coursera.org/learn/childnutrition/

Inspired by https://github.com/dgorissen/coursera-dl

## Running

Script uses same authorization method as `coursera-dl`, so add this line to `~/.netrc`

```
machine coursera-dl login YOUR_COURSERA_LOGIN password YOUR_COURSERA_PASWORD
```

You should also have Firefox web driver for Selenium installed. This is probably true if you have Firefox.

Then:

```
virtualenv ./env
source ./env/bin/activate
pip install -r ./requirements.txt
python cooking_dl
```
