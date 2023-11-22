from aiogram import Dispatcher, Bot
import asyncio
from config import TOKEN
from Core.handlers.routers import base_router, saving_router, sending_router



async def main():
    bot = Bot(TOKEN, parse_mode="HTML")

    dp = Dispatcher()
    dp.include_routers(base_router, saving_router, sending_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
