import discord
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

kumirei.run("MzIzNTYzMzI0MDUyODY1MDM0.DCAU2w.Tp3IB3Uv0chcv8vMqHgPkvmxOAY")
