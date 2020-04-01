# -*- coding:utf-8 -*-
import discord  # 라이브러리 임포트
import logging

from com.github.superjoy0502.clean.filtering.messageFiltering import *
from com.github.superjoy0502.clean.resources.token import getToken
import typing
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='resources/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()  # 인스턴스 만들기


@client.event  # 유니티로 따지면 Start()나 Update() 같은 어떤 스크립트 상의 이벤트
async def on_ready():  # 로그인
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):  # 메세지가 입력되었을 때
    if message.author == client.user:
        return
    if messagecheck(message.content, 금지어):
        filterMessage(message)


@bot.command()
async def test(ctx, arg):
    print("debug")
    await ctx.send(arg)


client.run(getToken())
