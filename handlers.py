from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove

from datetime import datetime

import keyboards as kb

router = Router()

results = []

username = ""

@router.message(Command("test"))
async def test_cmd(message: types.Message):
    print("✅ TEST команда получена!")
    await message.answer("Бот работает!")

def writing_logs(question, message):
    print('Записываю логи...')
    with open("C:\\vscodepj\\primer\\opr_logs.txt", "a", encoding="utf-8") as f:
        time = str(datetime.now())
        f.write(f"Время: {time[:19]}.  Имя пользователя - {username}. Вопрос: {question} - Ответ: {message}\n")

@router.message(Command("start"))
async def start(message: types.Message):
    global username
    username = message.from_user.full_name
    await message.answer("Добро пожаловать в опросник!", reply_markup=kb.start_menu)
    with open("opr_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"Имя пользователя - {username}")

@router.message(F.text == "⭐ Начать тест")
async def opr_start(message: types.Message):
    await message.answer("🎮 Играете ли вы в компьютерые игры?", reply_markup=kb.first_question)

@router.message(F.text == "✅ Да, играю.")
async def first_question_answer(message: types.Message):
    writing_logs("🎮 Играете ли вы в компьютерые игры?", "✅ Да, играю.")
    await message.answer("⏳ Сколько времени вы проводите за компьютером?", reply_markup=kb.second_question)
    results.append("✅ Вы играете в компьютерые игры.")

@router.message(F.text == "❌ Нет, не играю.")
async def first_question_answer(message: types.Message):
    writing_logs("🎮 Играете ли вы в компьютерые игры?", "❌ Нет, не играю.")
    await message.answer("Сколько времени вы проводите за компьютером?", reply_markup=kb.second_question)
    results.append("❌ Вы не играете в компьютерые игры.")

@router.message(F.text == "🕒 От 0 до 2 часов в день.")
async def second_question_answer(message: types.Message):
    writing_logs("⏳ Сколько времени вы проводите за компьютером?", "🕒 От 0 до 2 часов в день.")
    await message.answer("▶️ Смотрите ли Вы видео на Youtube?", 
                         reply_markup=kb.third_question)
    results.append("🕒 Вы проводите от 0 до 2 часов в день за компьютером.")

@router.message(F.text == "🕒 От 2 до 4 часов в день.")
async def second_question_answer(message: types.Message):
    writing_logs("⏳ Сколько времени вы проводите за компьютером?", "🕒 От 2 до 4 часов в день.")
    await message.answer("▶️ Смотрите ли Вы видео на Youtube?", 
                         reply_markup=kb.third_question)
    results.append("🕒 Вы проводите от 2 до 4 часов в день за компьютером.")

@router.message(F.text == "🕒 От 4 до 8 часов в день.")
async def second_question_answer(message: types.Message):
    writing_logs("⏳ Сколько времени вы проводите за компьютером?", "🕒 От 4 до 8 часов в день.")
    await message.answer("▶️ Смотрите ли Вы видео на Youtube?", 
                         reply_markup=kb.third_question)
    results.append("🕒 Вы проводите от 4 до 8 часов в день за компьютером.")
    
@router.message(F.text == "🕒 От 8 до 12+ часов в день.")
async def second_question_answer(message: types.Message):
    writing_logs("⏳ Сколько времени вы проводите за компьютером?", "🕒 От 8 до 12+ часов в день.")
    await message.answer("▶️ Смотрите ли Вы видео на Youtube?", 
                         reply_markup=kb.third_question)
    results.append("🕒 Вы проводите от 8 до 12+ часов в день за компьютером.")

@router.message(F.text == "✅ Да, смотрю.")
async def third_question_answer(message: types.Message):
    writing_logs("▶️ Смотрите ли Вы видео на Youtube?", "✅ Да, смотрю.")
    await message.answer("▶️ Сколько времени вы уделяете на промотр видео на Youtube?", 
                         reply_markup=kb.third_question_yes)

@router.message(F.text == "🕒 От 0 до 3 часов в день.")
async def four_yt_question_answer(message: types.Message):
    writing_logs("▶️ Сколько времени вы уделяете на промотр видео на Youtube?", "🕒 От 0 до 3 часов в день.")
    await message.answer("🎥 Любите ли вы смотреть фильмы?", reply_markup=kb.four_question)
    results.append("🎥 Вы уделяете от 0 до 3 часов в день на промотр видео на Youtube.")

@router.message(F.text == "🕒 От 3 до 6 часов в день.")
async def four_yt_question_answer(message: types.Message):
    writing_logs("▶️ Сколько времени вы уделяете на промотр видео на Youtube?", "🕒 От 3 до 6 часов в день.")
    await message.answer("🎥 Любите ли вы смотреть фильмы?", reply_markup=kb.four_question)
    results.append("🎥 Вы уделяете от 3 до 6 часов в день на промотр видео на Youtube.")

@router.message(F.text == "🕒 От 6 до 12+ часов в день.")
async def four_yt_question_answer(message: types.Message):
    writing_logs("▶️ Сколько времени вы уделяете на промотр видео на Youtube?", "🕒 От 6 до 12+ часов в день.")
    await message.answer("🎥 Любите ли вы смотреть фильмы?", reply_markup=kb.four_question)
    results.append("🎥 Вы уделяете от 6 до 12+ часов в день на промотр видео на Youtube.")

@router.message(F.text == "❌ Нет, не смотрю.")
async def third_question_answer(message: types.Message):
    writing_logs("▶️ Смотрите ли Вы видео на Youtube?", "❌ Нет, не смотрю.")
    await message.answer("🎥 Любите ли вы смотреть фильмы?", reply_markup=kb.four_question)
    results.append("🎥 Вы не смотрите Youtube")

@router.message(F.text == "💜 Мне нравятся смотреть фильмы!")
async def four_question_answer(message: types.Message):
    writing_logs("🎥 Любите ли вы смотреть фильмы?", "💜 Мне нравятся смотреть фильмы!")
    await message.answer("Отлично! Вы успешно прошли тестирование. Показать результаты?", 
                         reply_markup=kb.five_question)
    results.append("💜 Вы любите смотреть фильмы.")
    
@router.message(F.text == "❌ Мне это не интересно")
async def four_question_answer(message: types.Message):
    writing_logs("🎥 Любите ли вы смотреть фильмы?", "❌ Мне это не интересно")
    await message.answer("Отлично! Вы успешно прошли тестирование. Показать результаты?", 
                         reply_markup=kb.five_question)
    results.append("❌ Вам не нравится смореть фильмы.")

@router.message(F.text == "✅ Да, конечно!")
async def result(message: types.Message):
    writing_logs("📊 Показать результаты?", "✅ Да, конечно!")
    for i in results:
        await message.answer(i)
    await message.answer("Хотите начать тестирование сначала?", reply_markup=kb.again)

@router.message(F.text == "🔄")
async def restart_test(message: types.Message):
    await start(message)

@router.message(F.text == "❌")
async def cancel_restart(message: types.Message):
    await message.answer("Тестирование завершено! Если захотите начать заново - используйте /start", 
                         reply_markup=ReplyKeyboardRemove())