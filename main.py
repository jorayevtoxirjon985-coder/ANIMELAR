import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Railway Variables
TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Foydalanuvchi ismini olish
    user_name = message.from_user.first_name
    
    # Start berilganda chiqadigan matn
    welcome_text = (
        f"👋 Salom, {user_name}!\n\n"
        "Men sizga yordam berishga tayyorman. 🚀\n"
        "Men orqali quyidagilarni topishingiz mumkin:\n"
        "🎬 **Animelarning xohlagan qismini**\n"
        "🎥 **Kinolar va qisqa videolar**\n"
        "🎵 **Musiqa va rasmlar**\n\n"
        "Menga shunchaki nima qidirayotganingizni yozing (masalan: 'Naruto 10-qism' yoki 'Qiziqarli kinolar'). "
        "Men sizga darrov topib beraman!"
    )
    
    # Chiroyli tugmalar
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn_help = InlineKeyboardButton("ℹ️ Yordam", callback_data="help")
    btn_dev = InlineKeyboardButton("👨‍💻 Adminga yozish", url="https://t.me/j0rayev_3807")
    keyboard.add(btn_help, btn_dev)

    await message.answer(welcome_text, reply_markup=keyboard, parse_mode="Markdown")

@dp.message_handler()
async def universal_search(message: types.Message):
    query = message.text
    await message.answer(f"🔍 **'{query}'** bo'yicha qidiruv boshlandi...")

    # Saytlarga yo'naltirish tugmalari
    yt_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    google_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
    search_buttons = InlineKeyboardMarkup(row_width=1)
    search_buttons.add(
        InlineKeyboardButton("🎬 YouTubedan ko'rish", url=yt_url),
        InlineKeyboardButton("🌍 Googledan qidirish", url=google_url)
    )

    await message.answer(
        f"✅ Siz qidirgan: **{query}**\n\nNatijalarni ko'rish uchun quyidagi tugmalarni bosing:",
        reply_markup=search_buttons,
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
