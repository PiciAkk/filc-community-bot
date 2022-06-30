import discord
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
    elif "bázisolt" in message.content:
        await message.channel.send('Bázisolt? Bázisolt mire? A pöcsödre? Kérlek fogd már be és úgy használd a szavakat, ahogy kell, te kibaszott barlanglakó. Szerinted Isten azért adta a szólászabadságot, hogy random faszságot köpködj amik egyáltalán nem tartoznak a beszélgetés témájához? De komolyan, állandóan arra panaszkodsz, hogy senki nem beszélget veled vagy senki nem nem fejezi ki a véleményét rólad, mert random faszágokat magyarázol, mint pl pöggerek bázisolt kringé és amikor elmagyaráznád csak annyit mondasz, hogy hát vicces. Mi van? Mi a faszom vicces abban, hogy azt hiszed, hogy stand-up humorista leszel aki vastapsot kap, mert a színpadon kimondtad, hogy "geci"? MÉG MIT NEM TE ISTENTELEN BAROM, szóval kérlek pofa be és rendeltetésszerűen használd a szavakat te idóta kurva.')
    elif "amogus" in message.content:
        await message.channel.send(f"{message.author} szerintem sussy")
    

client.run(token)