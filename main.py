from aiogram import Bot,Dispatcher,executor,types
TOKEN_API="6049796693:AAGMP8YSgH9Npcmph1DdPujJDLkibuX_AMs" # авторизационный токен для получения телеграмм API
bot= Bot(TOKEN_API)
dp= Dispatcher(bot)

dp.message_handler()
async def echo(message:types.Message):
    await message.answer(text=message.text)

if __name__=='__main__':
    executor.start_polling(dp)