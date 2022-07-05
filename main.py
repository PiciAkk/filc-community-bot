import json
import discord
from discord import Intents, app_commands
import latex
import horoscope
import catto

horoszkop_csatorna = 992771006403985429
rangok_csatorna = 993630780532199536

CHANNEL_ID = #töltsd ki
MyGuild = discord.Object(id=0) #töltsd ki
class aclient(discord.Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MyGuild)
        await self.tree.sync(guild=MyGuild)


intents = Intents.all()
intents.members = True
intents.message_content = True


client = aclient(intents=intents)
token = open("token.txt", "r").read()

async def rossz_csatorna(aktualis_csatorna, jo_csatorna):
    await aktualis_csatorna.send(f"Kérlek használd a megfelelő csatornát: <#{jo_csatorna}> :)")

def rangok():
    rangok_fajl = open("roles.json", "r")

    return json.loads(rangok_fajl.read())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.tree.command()
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!horoszkop"):
        if message.channel.id == horoszkop_csatorna:
            try:
                await message.channel.send(horoscope.fetch(message.content.replace("!horoszkop ", "")))
            except Exception:
                await message.channel.send("Nem létező horoszkóp!")
        else:
            await rossz_csatorna(message.channel, horoszkop_csatorna)

    elif message.content.startswith("!latex") or message.content.startswith("! latex"):
        try:
            latex.save_image_from_latex(message.content.replace("!latex", ""))
            await message.channel.send(file=discord.File("images/compiled_latex.png"))
        except Exception:
            await message.channel.send("Érvénytelen LaTeX!")

    elif message.content.startswith("!cat"):
        catto.fetch(message.content.replace("!cat ", ""))
        await message.channel.send(file=discord.File("images/cat.gif"))

    elif message.content == "!rangok":
        if message.channel.id == rangok_csatorna:
            await message.channel.send("Elérhető rangok:")
            await message.channel.send("_ _")
            await message.channel.send("\n\n".join(
                map(
                    lambda rang:
                    f"Rang: {rang['name']}\n"
                    f"Leírás: {rang['description']}\n"
                    f"Parancs: `!rang {rang['role']}`\n",
                    rangok()
                )
            ))
        else:
            await rossz_csatorna(message.channel, rangok_csatorna)

    elif message.content.startswith("!rang"):
        if message.channel.id == rangok_csatorna:
            kert_rang = message.content.replace("!rang ", "")
            elerheto_rangok = rangok()

            if kert_rang in map(lambda rang: rang["role"], elerheto_rangok):
                await message.author.add_roles(discord.utils.get(message.guild.roles, name=kert_rang))
                await message.add_reaction(list(filter(lambda rang: rang["role"] == kert_rang, elerheto_rangok))[0]["emoji"])
        else:
            await rossz_csatorna(message.channel, rangok_csatorna)


client.run(token)
