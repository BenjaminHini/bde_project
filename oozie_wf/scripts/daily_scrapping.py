# import subprocess
# import sys

# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# for package in ["requests","bs4","pandas","numpy","datetime"]:
#     install(package)

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import date

ZODIAC_SIGNS = {
    "Aries": 1,
    "Taurus": 2,
    "Gemini": 3,
    "Cancer": 4,
    "Leo": 5,
    "Virgo": 6,
    "Libra": 7,
    "Scorpio": 8,
    "Sagittarius": 9,
    "Capricorn": 10,
    "Aquarius": 11,
    "Pisces": 12
}

def get_horoscope_by_day(zodiac_sign: int, day: str):
    if not "-" in day:
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}")
    else:
        day = day.replace("-", "")
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text

today = date.today()#for the database continuity
today_formated = "today"#for the http request
dates = 12* [today]
signs = []
descritpions = []
for sign in ZODIAC_SIGNS.values():
    signs.append(str(sign))
    descritpions.append(get_horoscope_by_day(sign, today_formated))

df = pd.DataFrame([dates, signs, descritpions]).T
df.columns = ['dates','signs','description']
df.to_json('daily_scrap.json')
df.to_csv('dail_scrap.csv')
