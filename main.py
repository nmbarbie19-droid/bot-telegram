import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# TOKEN DO BOT
TOKEN = "8323335001:AAFv3yD7Gy1DDFUB4kWPPBcyISc7V2bheOc"

# COMANDO /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    texto = """🔥 RESERVA VIP ATIVADA 🔥

💰 Valor VIP: R$19,99
🔑 Chave Pix: 11948212565

⚠️ Após pagar, envie qualquer mensagem aqui.
Assim que o Pix cair, liberamos seu acesso.

👇 Clique abaixo para continuar.
"""

    await update.message.reply_text(texto)


# INICIAR BOT
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("BOT ONLINE 🚀")

app.run_polling()
