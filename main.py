import discord
import latex
import horoscope
import catto

CHANNEL_ID = 992771006403985429

client = discord.Client()
token = open("token.txt", "r").read()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!horoszkop") and message.channel.id == CHANNEL_ID:
        try:
            await message.channel.send(horoscope.fetch(message.content.replace("!horoszkop ", "")))
        except Exception:
            await message.channel.send("Nem létező horoszkóp!")

    elif message.content.startswith("!horoszkop") and not message.channel.id == CHANNEL_ID:
        await message.channel.send(f"Kérlek használd a megfelelő csatornát: <#{CHANNEL_ID}> :)")
    
    elif message.content.startswith("!latex"):
        try:
            latex.save_image_from_latex(message.content.replace("!latex", ""))
            await message.channel.send(file=discord.File("compiled_latex.png"))
        except Exception:
            await message.channel.send("Érvénytelen LaTeX!")
    
    elif message.content.startswith("!cat"):
        catto.fetch(message.content.replace("!cat ", ""))
        await message.channel.send(file=discord.File("cat.gif"))

    elif message.content == "!gamer":
        await message.author.add_roles(discord.utils.get(message.guild.roles, name="gaymer"))

client.run(token)