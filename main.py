import os
from dotenv import load_dotenv

import discord
import ezcord

bot = ezcord.Bot(
    intents=discord.Intents.default(),
    error_webhook_url="WEBHOOK_URL",
)

if __name__ == "__main__":
    load_dotenv(".env")
    bot.load_cogs("cogs")
    bot.run(os.getenv("TOKEN"))
