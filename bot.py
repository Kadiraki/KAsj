import telebot

# Вставь сюда токен своего бота (получить в @BotFather)
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой бот. Задай мне вопрос 😊")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower()

    if "привет" in text:
        bot.reply_to(message, "Привет! Как дела?")
    elif "как дела" in text:
        bot.reply_to(message, "У меня всё отлично! А у тебя?")
    elif "пока" in text:
        bot.reply_to(message, "Пока! 👋")
    else:
        bot.reply_to(message, "Не совсем понял 😅 Попробуй спросить по-другому!")

print("Бот запущен...")
bot.infinity_polling()
