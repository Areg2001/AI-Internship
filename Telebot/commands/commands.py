from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command = 'start',
            description = "Sksi"
        ),
        BotCommand(
            command = 'help',
            description = "Help"
        ),

        BotCommand(
            command = "hello",
            description = "Baylus"
        ),
        BotCommand(
            command = "iphone",
            description = "Iphonner"
        ),
        BotCommand(
            command="by",
            description="Gnum"
        ),
        BotCommand(
            command="photo",
            description="Nkar"
        ),
        BotCommand(
            command="video",
            description="Video"
        ),
        BotCommand(
            command="document",
            description="Document"
        ),
        BotCommand(
            command="mediagroup",
            description="Nkar+Video"
        ),
        BotCommand(
            command="audio",
            description="audio"
        ),
        BotCommand(
            command="emojis",
            description="Smaylikner"
        ),
        BotCommand(
            command="url",
            description="url"
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())