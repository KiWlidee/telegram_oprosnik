import os
from asyncio import run as asrun
from aiogram import Bot, Dispatcher
from handlers import router

async def main():
    TOKEN = os.getenv('BOT_TOKEN')
    if not TOKEN:
        raise ValueError("BOT_TOKEN not found")
    
    print(f"✅ Бот запускается с токеном: {TOKEN[:10]}...")  # Логируем начало
    
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    
    print("✅ Роутеры подключены, начинаем polling...")
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# async def main():
#     TOKEN = os.getenv('BOT_TOKEN')
#     if not TOKEN:
#         raise ValueError("BOT_TOKEN not found in environment variables")
    
#     bot = Bot(token=TOKEN)
#     dp = Dispatcher()
#     dp.include_router(router)
    
#     # Очищаем webhook и запускаем polling
#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     try:
#         asrun(main())
#     except KeyboardInterrupt:
#         print("Бот остановлен")