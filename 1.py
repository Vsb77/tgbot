from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5746255962:AAH8gHCxcVXqx5XJ0wiKzbEzCiNaGcgll5E'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start (message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Получить сообщение")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Сообщение рассылки"
    )
    await message.answer("https://t.me/arbitragetrafficchat \n https://t.me/D_A_R_K_chat \n https://t.me/housedark \n https://t.me/Shades_of_traff \n https://t.me/combine_arbitrage_cpa \n https://t.me/Rush_Arbitration \n https://t.me/ChatForLeads \n https://t.me/TraffersChat \n https://t.me/BlackAffi \n https://t.me/t_raffik \n https://t.me/fbzonaruchat \n https://t.me/IKONA_TRAFF \n https://t.me/cpa4life \n https://t.me/fludilka_arbitrazhim \n https://t.me/Escrow22925 \n https://t.me/uslugiMasona \n https://t.me/facebookadsplus \n https://t.me/BlackMask113 \n https://t.me/skamilmamonta \n https://t.me/Business_Facebook \n https://t.me/cpamixSKAM \n https://t.me/MY1TRUST \n https://t.me/google_one_second", reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Получить сообщение")
async def without_puree(message: types.Message):
    await message.reply('Привет друг✋\nРады представить тебе канал по арбитражу трафика где мы собираем все мануалы по отливу на практически все направления и бесплатно публикуем материалы😎 которые другие "успешные арбитражники" продают на своих обучающих курсах.\nТакже можешь залететь в наш чатик где тебе всегда помогут)\nВ планах создать складчину всех полезных курсов.\nПрисоединяйся к нашему комьюнити 😊\nhttps://t.me/+QNCKxTIePPdiNmVi', reply_markup=types.ReplyKeyboardRemove())

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
