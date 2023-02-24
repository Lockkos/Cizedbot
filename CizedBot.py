import discord
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import requests, json, random
import time
import colorama
import pyautogui
from colorama import Fore
colorama.init()
import sys
from random import random
import threading
from threading import Thread
from time import sleep
import random
import socket, requests
from pypresence import Presence
import threading
import os
import string
import subprocess, requests, webbrowser
from urllib.request import urlopen
from getpass import getpass
from random import randint
import secrets
from getpass import getpass
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode   

client_id = "1078360668178231296"
RPC = Presence(client_id)
RPC.connect()

quotes =[
    "Frenpo CizedN3t",
    "CizedN3t",
    "Dm Me To Buy"
]

while True:
    RPC.update(details="Quote:", state=random.choice(quotes))
    time.sleep(5)


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.command()
async def methods(ctx):
    embed = discord.Embed(
        colour=discord.Colour.random(),
        description="1.udp-2.http3.",
        title="Methods"
        )
    embed.set_footer(text=f"Requested by {ctx.author.mention}")
    embed.set_author(name='NetWork')
    embed.set_thumbnail(url="https://www.greekmythology.com/images/mythology/poseidon_large_image_2.jpg")

    await ctx.send(embed=embed)

@client.command()
async def Help(ctx):
   author = ctx.message.author
   embed=discord.Embed(title="Help Commands", description="Commands",color=0x9208ea)
   embed.add_field(name="udp", value="Udp Layer")
   embed.add_field(name="http", value="http Layer")
   embed.add_field(name="ServerStats", value="see members")
   embed.add_field(name="Buyers Having Their On Commands", value="buyers")
   embed.set_footer(text="Help Commands")
   embed.set_thumbnail(url="https://www.greekmythology.com/images/mythology/poseidon_large_image_2.jpg")
   await ctx.send(embed=embed)




@client.command()
async def punch(ctx):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description=f"{ctx.author.mention} {(random.choice(punch_names))}"
    )
    embed.set_image(url=(random.choice(punch_gifs)))


    await ctx.send(embed=embed)

@client.command()
async def slap(ctx):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description=f"{ctx.author.mention} {(random.choice(slap_names))}"
    )
    embed.set_image(url=(random.choice(slap_gifs)))

    await ctx.send(embed=embed)


bot = commands.Bot(command_prefix="dog ")

@bot.command(name="hi")
async def SendMessage(ctx):
	await ctx.send('Hello!')

@bot.command(name="pic")
async def Dog(ctx):
	response = requests.get("https://media.tenor.com/DB5qwXcuerAAAAAM/anime-attack-ohto-ai.gif")
	image_link = response.json()["https://media.tenor.com/DB5qwXcuerAAAAAM/anime-attack-ohto-ai.gif"]
	await ctx.send(image_link)

@bot.command(name="gif", aliases=["feed", "play", "sleep"])
async def Gif(ctx):
	await ctx.send(random.choice(links[ctx.invoked_with]))

@client.command()
async def Udp(ctx):
    embed = discord.Embed(
        colour=discord.Colour.random(),
        description="**CizedN3t Udp Attack**",
        title="||Udp Attack ||"
        )

    embed.set_footer(text=f"CizedN3t Attack With Udp")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1052636774641442857/d227306ec2b8fa5ea52dfc0b17506336.webp?size=240")
    embed.set_author(name='CizedNetwork')
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
	print(f"Loggined in as: {bot.user.name}")

@client.command()
async def Methods(ctx):
    embed = discord.Embed(
        colour=discord.Colour.random(),
        description=f"""**-Methods** <a:1040668569568039022:1078582289434411119> Udp,Soc,Http,Tcp
        -**Url** <:8374_Telegram:1078581786629652570> Website:'t.me/CizedN3t'
        -**Author:**<a:protection:1078582358590095401> {ctx.author.mention}
        -**🛒Plan:Basic 10$**""",
        title="Methods For ||Attack||"
        )

    embed.set_footer(text="")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1052636774641442857/d227306ec2b8fa5ea52dfc0b17506336.webp?size=240")
    embed.set_author(name='NetWork Methods')
    await ctx.send(embed=embed)

@client.command()
async def plans(ctx):
   author = ctx.message.author
   embed=discord.Embed(title="Plans🛒", description="Plan",color=0xe74c3c)
   embed.add_field(name="Basic Plan", value="10€")
   embed.add_field(name="Vip Plan", value="20€")
   embed.add_field(name="LifeTime Plan", value="35€")
   embed.add_field(name="-**Basic Plan Is 100seconds Attack and 50gb Attack With Somecommands**", value="Basic Plan")
   embed.add_field(name="-**Vip Plan Is 500seconds Attack and 150gb Attack And More**", value="Vip Plan")
   embed.add_field(name="-**LifeTime Plan Is 1000seconds Attack and 300gb Attack**", value="LifeTime Plan")
   embed.set_footer(text="Plans🛒")
   embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1052636774641442857/d227306ec2b8fa5ea52dfc0b17506336.webp?size=240")
   await ctx.send(embed=embed)

@client.command()
async def t00ls(ctx):
    embed = discord.Embed(
        colour=discord.Colour.random(),
        description="""**Tools:
`Always On` <a:GreenVerifiedTick1:1078580170639814729>
------------------
Spotify G3nerator
G3nerators For All Services
dd0s panel
Tiktok Viewbot
Account N3ker
Bot Commands And N3ke Commands
Accounts For Services
Tiktok R3port Bot
Mass R3port
Mass Dm
Text Spamm3r
Methods For Accs and many applications
Account joiners
D0s To0ls 
Diamond T0ken Generator
Diamond Gen bot 
------------------
Payment Methods <:PayPal:1078408036961505391> / <:Paysafe:1078408105911668887>
 

<:Money_wings_AE:1078579744989257748> Im not responsible for what you do with these tools
Tools: Start with 5€-10€-15€

🎟️ Open A ticket To Buy

@everyone**""",
        title="||Tools🛒||"
        )

    embed.set_footer(text=f"Shop To0ls")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1052636774641442857/d227306ec2b8fa5ea52dfc0b17506336.webp?size=240")
    embed.set_author(name='To0ls')
    await ctx.send(embed=embed)





client.run("MTA3ODM2MDY2ODE3ODIzMTI5Ng.GxJVoG.Kl7WneYM2CMZuNJKU0aiKLhQfRbjTqzEliwrHk")