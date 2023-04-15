from aiogram import Bot,Dispatcher,executor,types #подключение библиотеки
TOKEN_API="6049796693:AAGMP8YSgH9Npcmph1DdPujJDLkibuX_AMs" # авторизационный токен для получения телеграмм API
bot = Bot(TOKEN_API)  # Инициализация бота
dp = Dispatcher(bot)  # Инициализация диспетчера
@dp.message_handler(commands=['start','help']) #создание обработчика для /start и /help
async def send_welcome(message:types.Message):
    await message.answer("<b>Здравствуйте!\nК какому врачу хотите записаться?</b>,\nВведите после /title", parse_mode="HTML")
@dp.message_handler(commands=['title'])  # Добавление специальности врача (/title)
async def title(message: types.Message):
    global arg
    arg = message.get_args() #ввод специальности врача
    with open('talon.txt','r') as f:
        coupons = f.read()
    await bot.send_message(message.chat.id,coupons)  # вывод списка талонов
    await message.answer("Введите номер талона после /talon")
@dp.message_handler(commands=['talon'])
async def talon(message: types.Message):
    n = int(message.get_args())  # ввод номера талона
    global date
    with open('talon.txt', 'r') as f: # присвоили переменной date дату из talon.txt под указанным номером
        date = f.readlines()[n - 1]
    f1=open('talon.txt','r').readlines() # удалили из файла talon.txt только что выбранную дату
    f1.pop(n-1)
    with open("talon.txt","w") as F:
        F.writelines(f1)
    await message.answer("Введите свою Фамилию И.О. после /name")
@dp.message_handler(commands=['name'])
async def talon(message: types.Message):
    global name
    name = message.get_args()  # Запрос ФИО пользователя
    with open('title.txt','a+') as file: # записали все даннные в title.txt
        file.write(f"{name} {arg} {date}")
    with open('title.txt', 'r') as F1:
        title = F1.readlines()[-1]
    await message.answer(f"Вы успешно записаны на приём. Запись:\n{title}")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
