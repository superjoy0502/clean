def messagecheck(message, li):  # 메세지에 금지어가 있는지 체크하는 용도
    for i in range(0, len(li)):
        if li[i] in message.lower():
            return 1
