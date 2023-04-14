from aiogram import Bot,Dispatcher,executor,types #подключение библиотеки
TOKEN_API="6049796693:AAGMP8YSgH9Npcmph1DdPujJDLkibuX_AMs" # авторизационный токен для получения телеграмм API
bot= Bot(TOKEN_API) # Инициализация бота
dp= Dispatcher(bot)# Инициализация диспетчера
@dp.message_handler(commands=['start','help']) #создание обработчика для /start и /help
async def send_welcome(message:types.Message):
    await message.answer("<b>Здравствуйте!\nК какому врачу хотите записаться?</b>,\nВведите после /title", parse_mode="HTML")



@dp.message_handler(commands=['title'])  # Добавление специальности врача (/title)
async def title(message: types.Message):
    arg = message.get_args()
    with open('title.txt', 'a') as file:  # создаём файл для записи в него выбора врача
        file.write(arg+'\t')
    with open('talon.txt', 'r') as f:
        coupons = f.read()
    await bot.send_message(message.chat.id,coupons)  # вывод списка талонов
    await message.answer("Введите номер талона после /talon")
@dp.message_handler(commands=['talon'])
async def talon(message: types.Message):
    n = int(message.get_args())  # ввод номера талона
    with open('talon.txt', 'r') as f:
        talon = f.readlines()
    choice = talon[n - 1]
    with open('title.txt', 'a') as file:
        file.write(choice)

@dp.message_handler(commands=['get'])          # Выгрузка специальности врача (/get)
async def get(message: types.Message):
    with open('title.txt', 'r') as f:
        title = f.readlines()[-1]
    await bot.send_message(message.chat.id, title)

if __name__ == '__main__':
    executor.start_polling(dp)
