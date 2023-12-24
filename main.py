import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from apikeys import *
from botCommands import *
from botHelp import *

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix='!', intents=intents)
bot.help_command = SupremeHelpCommand()

@bot.event
async def on_ready():
    print('Bot is ready!')
    print("-----------------------------------")

@bot.command(name='helplist', aliases=['h', 'H', 'commands'])
async def helpList(ctx):
    await ctx.send(HELPLIST)
    await ctx.send('For a more detailed list type help-list')

@bot.command(name='helplistExtended', aliases=['help-list'])
async def helplistExtended(ctx):
    await ctx.send(HELPLISTEXTENDED)
    
@bot.command(name='join', pass_content = True, aliases=['j'])
async def join(ctx):
    await joinServer(ctx)
    # if (ctx.author.voice):
    #     channel= ctx.message.author.voice.channel
    #     voice = await channel.connect()
    #     # source = FFmpegPCMAudio('Ultimate Glitch Hop Gaming Mix 2017 - Best Of Glitch Hop Music 2017 & All Time (128kbit_AAC).m4a')
    #     # player = voice.play(source)
    # else:
    #     await ctx.send("You must be in a voice channel to run this command (TEST)")

@bot.command(name='leave', pass_content = True, aliases=['l', 'fuckoff'])
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("You must be in a voice channel to run this command (TEST)")


@bot.command(name='pause', pass_content = True, aliases=['p'])
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("No audio or already paused")

@bot.command(name='resume', pass_content = True, aliases=['r'])
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Audio is already playing")

@bot.command(name='stop', pass_content = True, aliases=['s', 'shutup'])
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)
    await ctx.send('Stopping audio')
    voice.stop()

@bot.command(name='play', pass_content = True, aliases=[''])
async def play(ctx, arg):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio(arg)
        player = voice.play(source)





























bot.run(BOTTOKEN)