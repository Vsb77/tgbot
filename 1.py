from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5746255962:AAH8gHCxcVXqx5XJ0wiKzbEzCiNaGcgll5E'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome (message: types.Message):
   await message.answer("https://t.me/huntertraf \n https://t.me/google_arbitraj \n https://t.me/D_A_R_K_chat \n https://t.me/arbitrajcpa \n https://t.me/kupets_chat \n https://t.me/cparipchat\n https://t.me/housedark \n https://t.me/arbitragetrafficchat \n https://t.me/in_drks \n https://t.me/cparipchat\n https://t.me/google_arbitraj \n https://t.me/ads_traffic\n https://t.me/fbzonaruchat\n https://t.me/ChatForLeads\n https://t.me/arbitraj_vakansi\n https://t.me/cpaboard \nhttps://t.me/traffic_devils_chat\n https://t.me/traffic_devils_chat\n https://t.me/arbit_chat\n https://t.me/doska_fb\n https://t.me/pirate_cpa\n https://t.me/piratecpa\n https://t.me/TrafficMafiaChat\n https://t.me/ToxicKings_team\n https://t.me/kupets_chat\n https://t.me/cparipchat \nhttps://t.me/tooki_fb")

@dp.message_handler()
async def echo(message: types.Message):
   await message.answer('Привет друг✋\nРады представить тебе канал по арбитражу трафика где мы собираем все мануалы по отливу на практически все направления и бесплатно публикуем материалы😎 которые другие "успешные арбитражники" продают на своих обучающих курсах.\nТакже можешь залететь в наш чатик где тебе всегда помогут)\nВ планах создать складчину всех полезных курсов.\nПрисоединяйся к нашему комьюнити 😊\nhttps://t.me/+QNCKxTIePPdiNmVi')

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)