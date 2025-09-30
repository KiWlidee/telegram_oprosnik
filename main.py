import os
from asyncio import run as asrun
from aiogram import Bot, Dispatcher
from handlers import router

async def main():
    # Берем токен из переменных окружения
    TOKEN = os.getenv('BOT_TOKEN')
    if not TOKEN:
        raise ValueError("BOT_TOKEN not found in environment variables")
    
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asrun(main())
    except KeyboardInterrupt:
        print("Бот остановлен")