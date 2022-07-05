import requests
import json

def fetch(catto):
    image = open("images/cat.gif", "wb+")
    if len(catto) <= 3:
        image.write(requests.get(f"https://http.cat/{catto}").content)
    elif len(catto) > 3 and catto == "random":
        image.write(requests.get(requests.get("https://aws.random.cat/meow").json()["file"]).content)
    else:
        image.write(requests.get(f"https://http.cat/404").content)
    image.close()
