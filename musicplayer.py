import discord
import asyncio

client = discord.Client()

music = {
    'コマンド1':'音源.mp3',
    'コマンド2':'音源2.mp3'
}

@client.event
async def on_ready():
    print('{0.user}：いつでもいけるぜ'.format(client))

@client.event
async def on_message(message):
    global vc

    if message.content.startswith("/stop"):
        await message.delete()
        await vc.disconnect()

    if message.content in music:
        await message.delete()
        vc = await discord.VoiceChannel.connect(message.author.voice.channel)
        vc.play(discord.FFmpegPCMAudio(music[message.content]), after=None)
        await asyncio.sleep(0.5)
        while vc.is_playing() == True:
            await asyncio.sleep(0.2)
        await vc.disconnect()

    if vc.is_playing() == False:
        await vc.disconnect()

client.run("Token")