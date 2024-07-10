# meta developer: @modwini
from .. import loader
from asyncio import sleep


@loader.tds
class bro(loader.Module):
    strings = {"name": "hityka"}

    @loader.owner
    async def brocmd(self, message):
        for _ in range(1):
            for bro in ["бро ты...", лучший", "отмосферный", "кайфовый", " вайбовый", "никогда не бросай меня💋"]:
                await message.edit(bro)
                await sleep(0.3)
