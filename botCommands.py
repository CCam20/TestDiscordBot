import discord
from discord.ext import commands

async def joinServer(ctx):
        if (ctx.author.voice):
            channel= ctx.message.author.voice.channel
            voice = await channel.connect()
        # source = FFmpegPCMAudio('Ultimate Glitch Hop Gaming Mix 2017 - Best Of Glitch Hop Music 2017 & All Time (128kbit_AAC).m4a')
        # player = voice.play(source)
        else:
            await ctx.send("You must be in a voice channel to run this command (TEST)")