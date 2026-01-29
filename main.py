import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests # Saytlardan ma'lumot olish uchun

# Sozlamalar
TOKEN = os.getenv('BOT_TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.first_name}! 👋\n\nMen universal qidiruv botiman. Menga istalgan narsa (kino, video, rasm nomi)ni yozing, men uni saytlardan topib beraman!")

@dp.message_handler()
async def search_all(message: types.Message):
    query = message.text
    await message.answer("🔍 Qidiryapman, ozgina kuting...")

    # 1. YouTube-dan qidirish (Havoalarni olish)
    yt_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    
    # 2. Google-dan qidirish
    google_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

    # Tugmalarni yasash
    buttons = InlineKeyboardMarkup(row_width=1)
    btn_yt = InlineKeyboardButton("🎬 YouTube-dan ko'rish", url=yt_url)
    btn_gg = InlineKeyboardButton("🌍 Google-dan ma'lumot", url=google_url)
    buttons.add(btn_yt, btn_gg)

    # Natijani qaytarish
    text = f"✅ **{query}** bo'yicha natijalar tayyor:\n\n" \
           f"Pastdagi tugmalar orqali to'g'ridan-to'g'ri saytga o'tib tomosha qilishingiz mumkin."
    
    await message.answer(text, reply_markup=buttons, parse_mode="Markdown")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
