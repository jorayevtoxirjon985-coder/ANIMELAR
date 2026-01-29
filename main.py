import os
import logging
from aiogram import Bot, Dispatcher, executor, types

# Railway-dagi Variables'dan oladi
TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Siz xohlagandek universal start matni
    text = (
        f"👋 Salom {message.from_user.first_name}!\n\n"
        "Men sizga animelarning xohlagan qismini topib beraman! 🎬\n"
        "Faqat anime emas, boshqa narsa kerak bo'lsa ham topib beraman. 🚀\n\n"
        "Menga shunchaki nomini yozing, men darrov qidirishni boshlayman!"
    )
    await message.answer(text)

@dp.message_handler()
async def search(message: types.Message):
    query = message.text
    # Qidiruv linklarini yasash
    yt = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    gg = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🎬 YouTubedan topish", url=yt))
    markup.add(types.InlineKeyboardButton("🌍 Googledan topish", url=gg))
    
    await message.answer(f"🔍 '{query}' bo'yicha qidiruv natijalari:", reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
