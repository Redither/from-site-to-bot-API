import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
import telebot
import db

app = Flask(__name__)
CORS(app)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
bot_token = '6011770930:AAFgUjTWm5KyY31IEWr0Sr9x1Cyl8lhSOH4'
# chat_id = 'YOUR_TELEGRAM_CHAT_ID'
chat_id = '477297060'

# Создаем экземпляр бота
bot = telebot.TeleBot(bot_token)


# Обработчик для эндпоинта
@app.route('/ticket', methods=['POST'])
# @cross_origin()
def submit_form():
    name = request.form['name']
    phone = request.form['phoner']
    message = request.form['message']

    # Сохраняем данные в базу данных
    db.add_ticket(name, phone, message)
    print('Request saved to database')

    # Отправляем уведомление в телеграм
    message = f"New request:\nPhone number: {phone}\nMessage: {message}"
    bot.send_message(chat_id, message)

    return 'Request submitted'

# Запускаем сервер
if __name__ == '__main__':
    app.run()