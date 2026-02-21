from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8323335001:AAFv3yD7Gy1DDFUB4kWPPBcyISc7V2bheOc
"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Ver Oferta"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "🔥 Bem-vindo!\n\nClique abaixo para ver a oferta:",
        reply_markup=reply_markup
    )

async def resposta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    if texto == "Ver Oferta":
        await update.message.reply_text(
            "💎 Oferta Especial 💎\n\n"
            "Acesso completo por apenas R$19,90.\n\n"
            "Quer garantir agora?"
        )
    else:
        await update.message.reply_text("Clique no botão para continuar.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, resposta))

app.run_polling()
