# -*- coding:utf-8 -*-

words = open("resources/금지어.words", 'r', encoding='UTF8')
금지어 = words.read()
words.close()
금지어 = 금지어.split(',')
filter_level = 0


def messagecheck(message, li):  # 메세지에 금지어가 있는지 체크하는 용도
    for i in range(0, len(li)):
        if li[i] in message.lower():
            return 1


def filterMessage(message):
    await message.delete()
    await message.channel.send("금지어입니다! / RESTRICTED WORD!")
