import discord
from discord.ext import commands
import random
import youtube_dl
import os
from youtubesearchpython import VideosSearch

playlist = []

#ssh 

TOKEN = ''


client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Rani wajed akhay bro')


@client.command(name="join")
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f'Ani m3ak a bro, ping dialk { round(client.latency * 1000) } ms')


@client.command(name="leave")
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send(f'Thalla akhay bro')

@client.command(name="skip")
async def play(ctx,url):

    await ctx.send("skipit xD")



@client.command(name="play")
async def play(ctx,url):

        playlist.append(url)


        ctx.voice_client.stop()
        FFMPEG_OPTIONS={'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client


        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            if "youtube.com" not in url:
        
                videosSearch = VideosSearch(url, limit = 1)

                vid_link = videosSearch.result()["result"][0]['id']
                url = "https://www.youtube.com/watch?v=" + vid_link
                print(url)
            
            info = ydl.extract_info(url,download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)



@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send("7bes mosi9a")

client.run(TOKEN)