import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

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

array = pd.date_range(start='2022-1-1', periods=365)
# print(str(array[0]).split(' ')[0])
description = []
signs= []
dates = []
sign = 1


for i in range(365):
    signs.append(sign)
    date = str(array[i]).split(' ')[0]
    dates.append(date)
    description.append(get_horoscope_by_day(sign,date))
    print(i)

df = pd.DataFrame([dates,signs,description])
df.T.to_excel('data.xlsx',index=False)
