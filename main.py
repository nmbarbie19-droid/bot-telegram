from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8323335001:AAFv3yD7Gy1DDFUB4kWPPBcyISc7V2bheOc
"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["🔥 Quero Acessar"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "🔥 ACESSO VIP LIBERADO 🔥\n\n"
        "Conteúdo exclusivo e privado.\n"
        "Acesso imediato após pagamento.\n\n"
        "Clique abaixo para continuar 👇",
        reply_markup=reply_markup
    )

async def mensagens(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    if texto == "🔥 Quero Acessar":
        await update.message.reply_text(
            "💎 Últimas vagas disponíveis!\n\n"
            "Valor promocional: R$19,90\n\n"
            "Pagamento via PIX 👇"
        )

        await update.message.reply_text(
            "🔑 Chave PIX:\n"
            "SEU_EMAIL_OU_CHAVE_AQUI\n\n"
            "Envie o comprovante aqui no chat."
        )

    else:
        await update.message.reply_text("Clique no botão para continuar.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensagens))

app.run_polling()
