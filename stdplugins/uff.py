"""Emoji
Available Commands:
.uff """

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_ttl = range(0, 75)

    input_str = event.pattern_match.group(1)

    if input_str == "uff":

        await event.edit(input_str)

        animation_chars = [

            "U",
            "Uf",
            "Uff",
            "Ufffff",
            "Uffffff",
            "Ufffffff",
            "Uffffffff",
            "Ufffffffff",
            "Uffffffffff",
            "Ufffffffffff",
            "Uffffffffffff",
            "Ufffffffffffff",
            "Uffffffffffffff"
        ]

        for i in animation_ttl:

            await event.edit(animation_chars[i % 75])
