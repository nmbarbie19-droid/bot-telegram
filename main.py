            f"""
📸 Envie o comprovante aqui.

Após confirmação manual, enviaremos o acesso VIP.
"""
        )


import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "@Daylibarbie19_bot"

VALOR = "R$19,99"
PIX = "11948212565"

VIP_LINK = "https://t.me/seugrupovip"
PREVIEW_LINK = "https://t.me/seugrupoprevia"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"""🔥 RESERVA ATIVADA

💰 Valor VIP: {VALOR}
🔑 Chave Pix: {PIX}

⚠️ Após pagar, envie qualquer mensagem aqui.
Assim que o Pix cair, liberamos seu acesso."""
    )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):

    texto = update.message.text.lower()

    # Se o cliente falar que pagou
    if "paguei" in texto or "pix" in texto or "comprovante" in texto:
        await update.message.reply_text(
            f"""📸 Envie o comprovante aqui.

Após confirmação enviaremos seu acesso VIP:
{VIP_LINK}"""
        )

    # Se NÃO pagou (remarketing + prévia)
    else:
        await update.message.reply_text(
            f"""⏳ Estamos aguardando confirmação do pagamento.
