# meta developer: @modwini
from .. import loader
from asyncio import sleep


@loader.tds
class rap(loader.Module):
    strings = {"name": "kilogi"}

    @loader.owner
    async def rapcmd(self, message):
        for _ in range(1):
            for rap in ["бро ты...", лучший", "отмосферный", "кайфовый", " вайбовый", "никогда не бросай меня"]:
                await message.edit(bro)
                await sleep(0.3)
