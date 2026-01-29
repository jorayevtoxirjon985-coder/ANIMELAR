import os
from aiogram import Bot, Dispatcher, executor, types

# Railway Variables-dan tokenni olamiz
TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Siz xohlagandek hamma narsani topaman deydigan gap
    user = message.from_user.first_name
    text = (
        f"👋 Salom {user}!\n\n"
        "Men universal qidiruv botiman! 🚀\n"
        "Menga xohlagan narsangizni yozing (kino, video, rasm, ma'lumot).\n"
        "Men sizga hamma joydan topib beraman! ✨"
    )
    await message.answer(text)

@dp.message_handler()
async def universal_search(message: types.Message):
    query = message.text
    # Qidiruv linklari
    yt = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    gg = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🎬 Videolar (YouTube)", url=yt),
        types.InlineKeyboardButton("🌍 Ma'lumotlar (Google)", url=gg)
    )
    
    await message.answer(f"🔍 '{query}' bo'yicha natijalar:", reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
