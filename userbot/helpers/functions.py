#Making it easy....
#thanks to @ranger_op

import os
import re
import time
import urllib.request
import zipfile
from random import choice
import asyncio
import PIL.ImageOps
import requests
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import Channel, PollAnswer
from validators.url import url
from bs4 import BeautifulSoup
from asyncio import sleep
from emoji import get_emoji_regexp

import shlex
from os import getcwd
from os.path import basename, join
from textwrap import wrap
from typing import Optional, Tuple

import numpy as np

try:
    from colour import Color as asciiColor
except:
    os.system("pip install colour")
from PIL import Image, ImageDraw, ImageFont
from telethon.errors.rpcerrorlist import YouBlockedUserError


async def simpmusic(simp , QUALITY):
  search = simp
  headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
  html = requests.get('https://www.youtube.com/results?search_query='+search, headers=headers).text
  soup = BeautifulSoup(html, 'html.parser')
  for link in soup.find_all('a'):
    if '/watch?v=' in link.get('href'):
        # May change when Youtube Website may get updated in the future.
        video_link = link.get('href') 
        break
  video_link =  'http://www.youtube.com/'+video_link
  command = ('youtube-dl --extract-audio --audio-format mp3 --audio-quality ' + QUALITY + ' ' + video_link)	
  os.system(command)

song_dl = "youtube-dl --force-ipv4 --write-thumbnail -o './temp/%(title)s.%(ext)s' --extract-audio --audio-format mp3 --audio-quality {QUALITY} {video_link}"
thumb_dl = "youtube-dl --force-ipv4 -o './temp/%(title)s.%(ext)s' --write-thumbnail --skip-download {video_link}"
video_dl = "youtube-dl --force-ipv4 --write-thumbnail  -o './temp/%(title)s.%(ext)s' -f '[filesize<20M]' {video_link}"
name_dl = (
    "youtube-dl --force-ipv4 --get-filename -o './temp/%(title)s.%(ext)s' {video_link}"
)

async def simpmusicvideo(simp):
    search = simp
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    html = requests.get('https://www.youtube.com/results?search_query='+search, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        if '/watch?v=' in link.get('href'):
            # May change when Youtube Website may get updated in the future.
            video_link = link.get('href') 
            break    
    video_link =  'http://www.youtube.com/'+video_link
    command = ('youtube-dl -f "[filesize<20M]" ' +video_link)  
    os.system(command)


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


#convertion..

def convert_toimage(image):
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("./temp/temp.jpg", "jpeg")
    os.remove(image)
    return "./temp/temp.jpg"


async def convert_tosticker(image):
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("./temp/temp.webp", "webp")
    os.remove(image)
    return "./temp/temp.webp"
    
async def invert_colors(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save(endname)


async def flip_image(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.flip(image)
    inverted_image.save(endname)


async def grayscale(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.grayscale(image)
    inverted_image.save(endname)


async def mirror_file(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.mirror(image)
    inverted_image.save(endname)


async def solarize(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.solarize(image, threshold=128)
    inverted_image.save(endname)
    
    
#pranks....
#source - https://nekobot.xyz/api

    
async def iphonex(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={text}").json()
    mafia = r.get("message")
    mafiaurl = url(mafia)
    if not mafiaurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def baguette(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=baguette&url={text}"
    ).json()
    mafia = r.get("message")
    mafiaurl = url(mafia)
    if not mafiaurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"
    
    
async def threats(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=threats&url={text}").json()
    mafia = r.get("message")
    mafiaurl = url(mafia)
    if not mafiaurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def lolice(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=lolice&url={text}").json()
    mafia = r.get("message")
    mafiaurl = url(mafia)
    if not mafiaurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def trash(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=trash&url={text}").json()
    mafia = r.get("message")
    mafiaurl = url(mafia)
    if not mafiaurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def awooify(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=awooify&url={text}").json()
    mafia = r.get("message")
    mafiaurl = url(mafia)
    if not mafiaurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def trap(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trap&name={text1}&author={text2}&image={text3}"
    ).json()
    mafia = r.get("message")
    mafiaurl = url(mafia)
    if not mafiaurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(mafia).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def phcomment(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=phcomment&image={text1}&text={text2}&username={text3}"
    ).json()
    mafia = r.get("message")
    mafiaurl = url(mafia)
    if not mafiaurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"

#tweets...
#source - https://nekobot.xyz/api

async def trumptweet(text):
        r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}").json()
        wew = r.get("message")
        hburl = url(wew)
        if not hburl:
            return  "check syntax once more"
        with open("temp.png", "wb") as f:
            f.write(requests.get(wew).content)
        img = Image.open("temp.png").convert("RGB")
        img.save("temp.jpg", "jpeg")    
        return "temp.jpg"

async def changemymind(text):
        r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}").json()
        wew = r.get("message")
        hburl = url(wew)
        if not hburl:
            return  "check syntax once more"
        with open("temp.png", "wb") as f:
            f.write(requests.get(wew).content)
        img = Image.open("temp.png").convert("RGB")
        img.save("temp.jpg", "jpeg")    
        return "temp.jpg"
    
async def kannagen(text):
        r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=kannagen&text={text}").json()
        wew = r.get("message")
        hburl = url(wew)
        if not hburl:
            return  "check syntax once more"
        with open("temp.png", "wb") as f:
            f.write(requests.get(wew).content)
        img = Image.open("temp.png").convert("RGB")
        img.save("temp.webp", "webp")    
        return "temp.webp"    
    
async def moditweet(text):
        r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=narendramodi").json()
        wew = r.get("message")
        hburl = url(wew)
        if not hburl:
            return  "check syntax once more"
        with open("temp.png", "wb") as f:
            f.write(requests.get(wew).content)
        img = Image.open("temp.png").convert("RGB")
        img.save("temp.jpg", "jpeg")    
        return "temp.jpg"    
        
        
async def miatweet(text):
        r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=miakhalifa").json()
        wew = r.get("message")
        hburl = url(wew)
        if not hburl:
            return  "check syntax once more"
        with open("temp.png", "wb") as f:
            f.write(requests.get(wew).content)
        img = Image.open("temp.png").convert("RGB")
        img.save("temp.jpg", "jpeg")    
        return "temp.jpg"    


async def papputweet(text):
        r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=rahulgandhi").json()
        wew = r.get("message")
        hburl = url(wew)
        if not hburl:
            return  "check syntax once more"
        with open("temp.png", "wb") as f:
            f.write(requests.get(wew).content)
        img = Image.open("temp.png").convert("RGB")
        img.save("temp.jpg", "jpeg")    
        return "temp.jpg"

async def sunnytweet(text):
        r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=sunnyleone").json()
        wew = r.get("message")
        hburl = url(wew)
        if not hburl:
            return  "check syntax once more"
        with open("temp.png", "wb") as f:
            f.write(requests.get(wew).content)
        img = Image.open("temp.png").convert("RGB")
        img.save("temp.jpg", "jpeg")    
        return "temp.jpg"    
    
    
async def tweets(text1,text2):
        r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=tweet&text={text1}&username={text2}").json()
        wew = r.get("message")
        hburl = url(wew)
        if not hburl:
            return  "check syntax once more"
        with open("temp.png", "wb") as f:
            f.write(requests.get(wew).content)
        img = Image.open("temp.png").convert("RGB")
        img.save("temp.jpg", "jpeg")    
        return "temp.jpg"    
