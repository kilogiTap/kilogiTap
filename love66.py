# meta developer: @hityka
from .. import loader
from asyncio import sleep


@loader.tds
class rap(loader.Module):
    strings = {"name": "влад пидор"}

    @loader.owner
    async def rapcmd(self, message):
        for _ in range(1):
            for rap in ["ты..  ", "лучшая", "самая красивая", "очень добрая", " ахуенная", "и", "я",
"тебя", "очень", " сильно", "люблю"]:
                await message.edit(rap)
                await sleep(0.3)
