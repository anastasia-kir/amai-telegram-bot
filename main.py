import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

MENU = [
    ["🍱 Меню", "💧 Вода"],
    ["📆 Привычки", "✨ Мотивация"],
    ["📝 Дневник", "📊 Статистика"],
    ["🧘 Медитация", "🌙 Вечер"],
    ["📚 Книги и Музыка", "💌 Обратная связь"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌸 Привет! Я — Amai, твой персональный ритуальный помощник! 🪷\n\n"
        "Я помогу тебе:\n"
        "✅ Планировать своё питание 🍱\n"
        "✅ Следить за уровнем воды в организме 💧\n"
        "✅ Формировать полезные привычки 📆\n"
        "✅ Получать ежедневную мотивацию ✨\n"
        "✅ Вести личный дневник 📝\n\n"
        "Готов(-а) начать путь к осознанности и балансу?\n"
        "Выбери, с чего хочешь начать 👇",
        reply_markup=ReplyKeyboardMarkup(MENU, resize_keyboard=True)
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = "Эта функция пока в разработке 💡"
    if text == "💧 Вода":
        response = "💧 Напоминаю: Пора выпить воды! Цель на день: 2 литра."
    elif text == "✨ Мотивация":
        response = "✨ Ты сильнее, чем думаешь. Продолжай двигаться вперёд!"
    elif text == "📝 Дневник":
        response = "Как ты себя чувствуешь сегодня? Напиши сюда, чтобы я сохранил это для тебя."
    elif text == "📊 Статистика":
        response = "📈 На этой неделе ты выпил 9 литров воды и завершил 12 привычек!"
    elif text == "📆 Привычки":
        response = "Добавь или отметь выполненные привычки сегодня."
    elif text == "🍱 Меню":
        response = "Выбери рецепты и составь меню. Я помогу собрать список покупок."
    elif text == "🧘 Медитация":
        response = "🧘 Таймер медитации на 3 минуты запущен... Дыши глубоко."
    elif text == "🌙 Вечер":
        response = "Что ты сегодня сделал? За что ты благодарен? Завтра будет новый шанс 🌙"
    elif text == "📚 Книги и Музыка":
        response = "📚 Рекомендации: 'Атомные привычки', 'Тонкое искусство пофигизма' 🎶 Музыка: Lo-Fi Chill"
    elif text == "💌 Обратная связь":
        response = "Оставь пожелания или идеи — я обязательно передам их создателю!"
    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == "__main__":
    main()