from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8323335001:AAFv3yD7Gy1DDFUB4kWPPBcyISc7V2bheOc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Recebeu /start")
    await update.message.reply_text("🔥 BOT ONLINE E FUNCIONANDO!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
