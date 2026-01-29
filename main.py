import os
import logging
from aiogram import Bot, Dispatcher, executor, types

# Railway Variables-dan olamiz
TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Foydalanuvchi ismini olamiz
    user = message.from_user.first_name
    
    # Siz xohlagandek universal start matni
    text = (
        f"👋 Salom {user}! Xush kelibsiz!\n\n"
        "Men sizga har qanday narsani topib beruvchi universal botman! 🚀\n\n"
        "Menga shunchaki nomini yozing, men sizga topib beraman:\n"
        "🎬 **Eng sara kinolar va seriallar**\n"
        "🎞 **Yangi animelar (barcha qismlari)**\n"
        "🧸 **Multfilmlar va qisqa videolar**\n"
        "🖼 **Chiroyli rasm va oboylar**\n"
        "🎵 **Musiqa va kliplar**\n\n"
        "Nima qidiramiz? Nomini yozing va yuboring! 👇"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message_handler()
async def universal_search(message: types.Message):
    query = message.text
    await message.answer(f"🔍 **'{query}'** bo'yicha eng yaxshi natijalarni qidiryapman...")

    # Qidiruv linklari (YouTube va Google orqali)
    yt = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    gg = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
    # Tugmalar
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🎬 Videoni tomosha qilish (YouTube)", url=yt),
        types.InlineKeyboardButton("🌍 Internetdan qidirish (Google)", url=gg)
    )
    
    await message.answer(
        f"✅ **{query}** bo'yicha natijalar tayyor!\n\n"
        "Ko'rish uchun tugmani bosing:", 
        reply_markup=markup,
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
