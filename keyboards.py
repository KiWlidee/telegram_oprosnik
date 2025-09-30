from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="⭐ Начать тест")
]], resize_keyboard=True)

first_question = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="✅ Да, играю."), KeyboardButton(text="❌ Нет, не играю.")
]], resize_keyboard=True)

second_question = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="🕒 От 0 до 2 часов в день."), 
    KeyboardButton(text="🕒 От 2 до 4 часов в день."),
    KeyboardButton(text="🕒 От 4 до 8 часов в день."),
    KeyboardButton(text="🕒 От 8 до 12+ часов в день."),
]], resize_keyboard=True)

third_question = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="✅ Да, смотрю."), 
    KeyboardButton(text="❌ Нет, не смотрю.")
]], resize_keyboard=True)

third_question_yes = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="🕒 От 0 до 3 часов в день."),
    KeyboardButton(text="🕒 От 3 до 6 часов в день."),
    KeyboardButton(text="🕒 От 6 до 12+ часов в день."),  
]], resize_keyboard=True)

four_question = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="💜 Мне нравятся смотреть фильмы!"),
    KeyboardButton(text="❌ Мне это не интересно")
]], resize_keyboard=True)

five_question = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="✅ Да, конечно!")
]], resize_keyboard=True)

again = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="🔄"),
    KeyboardButton(text="❌")
]], resize_keyboard=True)