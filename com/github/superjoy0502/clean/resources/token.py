# -*- coding:utf-8 -*-

token = open("resources/token.tk", 'r', encoding='UTF8')
token = token.read()
token.close()


def getToken():
    return token


def setToken(tk):
    token = tk
