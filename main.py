import os
import logging
from aiogram import Bot, Dispatcher, executor, types

# Railway Variables-dan tokenni olamiz
TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Siz xohlagan universal va kuchli start matni
    user = message.from_user.first_name
    text = (
        f"👋 Salom {user}!\n\n"
        "Men universal qidiruv botiman! ✨\n"
        "Menga xohlagan narsangizning nomini yozing, men sizga hamma joydan topib beraman.\n\n"
        "🚀 **Nimalarni topa olaman?**\n"
        "🔹 Istalgan kino va seriallar\n"
        "🔹 Videolar va kliplar\n"
        "🔹 O'yin va programmalar\n"
        "🔹 Rasmlar va kerakli ma'lumotlar\n\n"
        "🔍 Shunchaki nomini yozing va yuboring!"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message_handler()
async def search_engine(message: types.Message):
    query = message.text
    # Qidiruvni boshlash haqida xabar
    await message.answer(f"🔎 **{query}** bo'yicha eng yaxshi natijalarni qidiryapman...")

    # Qidiruv linklari (Hamma narsani qidiradi)
    yt_link = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    google_link = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    telegram_link = f"https://t.me/share/url?url=https://t.me/search?q={query.replace(' ', '+')}"
    
    # Tugmalar paneli
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🎬 Videolarni ko'rish (YouTube)", url=yt_link),
        types.InlineKeyboardButton("🌍 Internetdan topish (Google)", url=google_link),
        types.InlineKeyboardButton("🔍 Telegramdan qidirish", url=telegram_link)
    )
    
    await message.answer(
        f"✅ **{query}** uchun topilgan natijalar:\n\n"
        "Kerakli bo'limni tanlang 👇", 
        reply_markup=markup,
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
