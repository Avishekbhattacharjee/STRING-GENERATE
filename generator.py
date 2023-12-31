import logging
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, AccessTokenInvalid, ApiIdPublishedFlood
from Config import Config


logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
    ":memory:",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="StringSessionBot"),
)


# Run Bot
if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"Hey! Welcome to the bot @{uname} ")
    print("🔰Support Group🔰 [LOGS] : @TheDevsChats")
    print("⚜️Update Group⚜️  [LOGS] : @TheTelegramBotz")
    print(f"✨Bot Username [LOGS] :@{uname}!")
    print("Follow all the commands!")
    idle()
    app.stop()
    print("⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️")
    print("Bot Stopped")
    print(f"✨Bot Username✨ [LOGS] :@{uname}")
    print("⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️")
