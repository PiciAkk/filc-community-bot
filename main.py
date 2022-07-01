import discord
import latex
import horoscope

client = discord.Client()
token = open("token.txt", "r").read()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!horoszkop"):
        try:
            await message.channel.send(horoscope.fetch(message.content.replace("!horoszkop ", "")))
        except Exception:
            await message.channel.send("Nem létező horoszkóp!")
    elif message.content.startswith("!latex"):
        latex.save_image_from_latex(message.content.replace("!latex", ""))
        await message.channel.send(file=discord.File("compiled_latex.png"))

client.run(token)