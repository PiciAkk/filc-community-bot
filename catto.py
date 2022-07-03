import requests
import json
import case_sensitive

def fetch(catto):
    image = open("cat.gif", "wb+")
    catto = case_sensitive.transform(["!cat","! cat"],catto)
    if len(catto) == 3:
        image.write(requests.get(f"https://http.cat/{catto}").content)
    elif catto == "random":
        image.write(requests.get(requests.get("https://aws.random.cat/meow").json()["file"]).content)
    else:
        image.write(requests.get(f"https://http.cat/404").content)
    image.close()
