import uwufier
import json
import discord
import latex
import horoscope
import catto
import parse_message

horoszkop_csatorna = 992771006403985429
rangok_csatorna = 993630780532199536

client = discord.Client()
token = open("token.txt", "r").read()


async def rossz_csatorna(aktualis_csatorna, jo_csatorna):
    await aktualis_csatorna.send(f"Kérlek használd a megfelelő csatornát: <#{jo_csatorna}> :)")

def rangok():
    rangok_fajl = open("roles.json", "r")
    tartalom = rangok_fajl.read()
    
    rangok_fajl.close()

    return json.loads(tartalom)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user or not message.content.startswith("!"):
        return

    elemzett = parse_message.parse_message(message.content)

    match elemzett:
        case ["horoszkop", csillagkep]:            
            if message.channel.id == horoszkop_csatorna:
                try:
                    await message.channel.send(horoscope.fetch(csillagkep))
                except Exception:
                    await message.channel.send("Nem létező horoszkóp!")
            else:
                await rossz_csatorna(message.channel, horoszkop_csatorna)

        case ["latex", *latex_bemenet]:
            try:
                latex.save_image_from_latex(" ".join(latex_bemenet))
                await message.channel.send(file=discord.File("images/compiled_latex.png"))
            except Exception:
                await message.channel.send("Érvénytelen LaTeX!")
    
        case ["cat", kod]:
            catto.fetch(kod)
            await message.channel.send(file=discord.File("images/cat.gif"))

        case ["rang"|"rangok"]:
            if message.channel.id == rangok_csatorna:
                await message.channel.send("Elérhető rangok:")
                await message.channel.send("_ _")
                await message.channel.send("\n\n".join(
                    map(
                        lambda rang: 
                        f"**Rang:** {rang['name']}\n"
                        f"**Leírás:** {rang['description']}\n"
                        f"**Parancs:** `!rang {rang['role']}`\n",
                        rangok()
                    )
                ))
            else:
                await rossz_csatorna(message.channel, rangok_csatorna)

        case ["rang", kert_rang]:
            if message.channel.id == rangok_csatorna:
                elerheto_rangok = rangok()

                if kert_rang in map(lambda rang: rang["role"], elerheto_rangok):
                    await message.author.add_roles(discord.utils.get(message.guild.roles, name=kert_rang))
                    await message.add_reaction(list(filter(lambda rang: rang["role"] == kert_rang, elerheto_rangok))[0]["emoji"])
            else:
                await rossz_csatorna(message.channel, rangok_csatorna)

        case ["uwufy", *szoveg]:
            await message.channel.send(uwufier.uwufy(" ".join(szoveg)))

        case _:
            await message.channel.send("Ismeretlen parancs!")
            

client.run(token)
