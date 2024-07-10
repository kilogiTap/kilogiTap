# канал @kilogiSoft
from .. import loader


@loader.tds
class hihihaha(loader.Module):
    """кружок с птичкой
hityka pidor"""

    strings = {"name": "bird"}

    async def hihicmd(self, message):
        """Отпровляет кружок с птичкой"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/c/2064466349/242",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
