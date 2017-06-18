import discord
import random
import time
from discord.ext.commands import Bot


kumirei = Bot(command_prefix="->")


@kumirei.event
async def on_read():
    print("こんにちは！")


@kumirei.command()
async def hello(*args):
    return await kumirei.say("ちわっす！")


@kumirei.command()
async def song(*args):
    pass


@kumirei.command()
async def mood(*args):
    moods = ["悲しいです。。。", "今は幸せって感じ＾＾～", "泣きたい。。", "恋してるぅぅぅぅぅ", "怒ってます！"]
    return await kumirei.say(moods[random.randint(0,len(moods) - 1)])


@kumirei.command()
async def dice(*args):
    await kumirei.say("行くよ～")
    faces = [1, 2, 3, 4, 5, 6]
    value = faces[random.randint(0, len(faces) - 1)]
    for item in faces:
        if item == value:
            return await kumirei.say("{}　でした！")


@kumirei.command()
async def omikuji(*args):
    await kumirei.say("はい！おみくじを引くよ～\n今日の運は。。。")
    luck = ["大凶", "凶", "小吉", "大吉", "小凶", "吉"]
    return await kumirei.say(luck[(random.randint(0, len(luck) - 1))] + "でした！")

kumirei.run("MzIzNTYzMzI0MDUyODY1MDM0.DCAU2w.Tp3IB3Uv0chcv8vMqHgPkvmxOAY")
