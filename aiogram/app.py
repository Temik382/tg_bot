from aiogram import Bot, Dispatcher, types
from comons.cmd import private
import asyncio, os
from handlers.user_private import user_private_router

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_router(user_private_router)



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)

asyncio.run(main())