import requests

def fetch(catto):
    image = open("images/cat.gif", "wb+")

    if catto.isnumeric() and len(catto) <= 3:
        url = f"https://http.cat/{catto}"

    elif catto == "random":
        url = requests.get("https://aws.random.cat/meow").json()["file"]

    else:
        url = "https://http.cat/404"

    image.write(requests.get(url).content)
    image.close()
