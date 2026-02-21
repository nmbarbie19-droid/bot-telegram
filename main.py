import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("8323335001:AAFv3yD7Gy1DDFUB4kWPPBcyISc7V2bheOc")  # ou coloca direto o token aqui

VIP_LINK = "https://t.me/seugrupovip"
PREVIEW_LINK = "https://t.me/seugrupoprevia"

VALOR = "R$19,99"
PIX = "11948212565"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 Comprar VIP", callback_data="comprar")],
        [InlineKeyboardButton("👀 Ver Prévia Grátis", callback_data="previa")],
        [InlineKeyboardButton("✅ Já Paguei", callback_data="paguei")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    texto = f"""
🔥 *ACESSO VIP LIBERADO*

💰 Valor: {VALOR}
🔑 Chave Pix: `{PIX}`

Após pagar, clique em *Já Paguei*.
"""

    await update.message.reply_text(texto, parse_mode="Markdown", reply_markup=reply_markup)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "comprar":
        await query.edit_message_text(
            f"""
🔥 *FINALIZAR PAGAMENTO*

💰 Valor: {VALOR}
🔑 Pix: `{PIX}`

Após pagar, clique em *Já Paguei*.
""",
            parse_mode="Markdown"
        )

    elif query.data == "previa":
        await query.edit_message_text(
            f"""
👀 *Grupo de Prévia Liberado*

Entre aqui:
{PREVIEW_LINK}

Quando decidir comprar, clique novamente em /start
"""
        )

    elif query.data == "paguei":
        await query.edit_message_text(
            f"""
📸 Envie o comprovante aqui.

Após confirmação manual, enviaremos o acesso VIP.
"""
        )


async def comprovante_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"""
⏳ Comprovante recebido.

Assim que confirmado, enviaremos o link VIP.
"""
    )

    # Aqui você pode depois manualmente liberar
    # ou automatizar se quiser no futuro


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT | filters.PHOTO, comprovante_handler))

    print("Bot rodando igual máquina 💰🔥")
    app.run_polling()


if __name__ == "__main__":
    main()
