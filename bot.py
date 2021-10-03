import discord
from discord.ext import commands
import random
import youtube_dl
import os
from token import *


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


@client.command(name="quote")
async def quote(ctx):
    quotes = [
        "Live as if you were to die tomorrow. Learn as if you were to live forever.",

        "That which does not kill us makes us stronger.",

        "Be who you are and say what you feel, because those who mind don’t matter and those who matter don’t mind.",

        "We must not allow other people’s limited perceptions to define us.",
        "Do what you can, with what you have, where you are.",

        "Be yourself; everyone else is already taken.",

        "This above all: to thine own self be true.",

        "If you cannot do great things, do small things in a great way.",

        "If opportunity doesn’t knock, build a door.",

        "Wise men speak because they have something to say; fools because they have to say something.",

        "Strive not to be a success, but rather to be of value.",

        "Two roads diverged in a wood, and I—I took the one less traveled by, And that has made all the difference.",

        "Do not let what you cannot do interfere with what you can do.",

        "A journey of a thousand leagues begins beneath one’s feet.",

        "I’ve learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",

        "Either you run the day, or the day runs you.",

        "Life shrinks or expands in proportion to one’s courage.",

        "You must be the change you wish to see in the world.",

        "What you do speaks so loudly that I cannot hear what you say.",

        "Believe and act as if it were impossible to fail.",

        "The difference between ordinary and extraordinary is that little extra.",


        "The best way to predict the future is to invent it.",

        "If I am not for myself, who is for me? And if I am only for myself, what am I? And if not now, when?",

        "Everything has beauty, but not everyone can see.",

        "Self-reverence, self-knowledge, self control — these three alone lead to power.",

        "hough no one can go back and make a brand new start, anyone can start from now and make a brand new ending.",

        "Anyone who stops learning is old, whether at twenty or eighty. Anyone who keeps learning stays young. The greatest thing in life is to keep your mind young.",

        "He who angers you conquers you.",

        "Beauty, without expression, tires.",

        "The secret of business is to know something that nobody else knows.",
        "The greatest discovery of all time is that a person can change his future by merely changing his attitude.",
        "We cannot always build the future of our youth, but we can build our youth for the future.",

        "It takes courage to grow up and turn out to be who you really are.",
        "In this world nothing can be said to be certain, except death and taxes.",

        "It is the mark of an educated mind to be able to entertain a thought without accepting it.",

        "A happy family is but an earlier heaven.",

        "Don’t walk in front of me, I may not follow. Don’t walk behind me, I may not lead. Walk beside me and be my friend.",
        "Courage doesn’t always roar. Sometimes courage is the little voice at the end of the day that says ‘I’ll try again tomorrow.'",
        "Education is like a double-edged sword. It may be turned to dangerous uses if it is not properly handled.",

        "Walking with a friend in the dark is better than walking alone in the light.",

        "Happiness is not a goal; it is a by-product.",

        "Always forgive your enemies; nothing annoys them so much.",

        "The only true wisdom is knowing that you know nothing.",
        "As a well-spent day brings happy sleep, so a life well spent brings happy death.",

        "Courage is what it takes to stand up and speak. Courage is also what it takes to sit down and listen.",

        "Children are our most valuable resource.",

        "Love is, above all else, the gift of oneself.",

        "Music in the soul can be heard by the universe.",

        "Peace begins with a smile.",

        "Success is liking yourself, liking what you do, and liking how you do it.",

        "A friend is someone who knows all about you and still loves you.",

        "Never leave that till tomorrow which you can do today.",

        "If you don’t make mistakes, you’re not working on hard enough problems.",

        "We must learn to live together as brothers or perish together as fools.",

        "Life is like a camera. Just focus on what’s important, capture the good times, develop from the negatives, and if things don’t work out, just take another shot.",

        "When you judge another, you do not define them; you define yourself.",

        "Opportunity is missed by most people because it is dressed in overalls and looks like work.",

        "Love me when I least deserve it, because that’s when I really need it.",

        "The best and most beautiful things in the world cannot be seen or even touched. They must be felt with the heart.",

        "If you want to test your memory, try to recall what you were worrying about one year ago today.",

        "The real opportunity for success lies within the person and not in the job.",

        "It takes a great deal of courage to stand up to your enemies, but even more to stand up to your friends.",

        "Defeat is not bitter unless you swallow it.",

        "A mind is like a parachute. It doesn’t work if it isn’t open.",

        "The man who removes a mountain begins by carrying away small stones.",

        "When you are totally at peace with yourself, nothing can shake you.",

        "Be a first rate version of yourself, not a second rate version of someone else.",

        "Your worth consists in what you are and not in what you have.",

        "Others can stop you temporarily – you are the only one who can do it permanently.",

        "Life has no limitations, except the ones you make.",

        "Peace comes from within. Do not seek it without."]
    await ctx.send(f'{random.choice(quotes)}')


@client.command(name="play")
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await ctx.send("play dakchi dl mosi9a")
    #await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send("7bes mosi9a")

client.run(TOKEN)