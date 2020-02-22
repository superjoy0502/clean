# -*- coding:utf-8 -*-
import discord  # 라이브러리 임포트
import logging

from com.github.superjoy0502.clean.messageFiltering import *
import typing
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()  # 인스턴스 만들기
words = open("금지어.words", 'r', encoding='UTF8')
금지어 = words.read()
words.close()
금지어 = 금지어.split(',')
filter_level = 0


@client.event  # 유니티로 따지면 Start()나 Update() 같은 어떤 스크립트 상의 이벤트
async def on_ready():  # 로그인
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):  # 메세지가 입력되었을 때
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if messagecheck(message.content, 금지어):
        await message.delete()
        await message.channel.send("금지어입니다! / RESTRICTED WORD!")


@bot.command()
async def test(ctx, arg):
    print("debug")
    await ctx.send(arg)


client.run('Njc0ODE4NDY3NTYzNzAwMjQ0.XjupgA.c76Gr_TDRChOJtSVjYfCckJK1mU')
