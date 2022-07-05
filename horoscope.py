import unidecode
import requests

horoscopes = "kos,bika,ikrek,rak,oroszlan,szuz,merleg,skorpio,nyilas,bak,vizonto,halak".split(",")

def prepare(string):
    return unidecode.unidecode(string).lower()

def get_url(horoscope):
    if prepare(horoscope) not in horoscopes:
        raise Exception("Invalid horoscope!")

    return f"https://www.astronet.hu/horoszkop/{prepare(horoscope)}-napi-horoszkop/"

def fetch(horoscope):
    html = requests.get(get_url(horoscope)).content.decode("utf-8")

    start = html.find('<div class="details-content">') + 29
    end = html[start::].find('</div>') + start

    return html[start:end]