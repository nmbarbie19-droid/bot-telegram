from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

users = {}

VALOR = "R$19,99"
PIX = "11948212565"
LINK_GRUPO = "https://t.me/SEUGRUPO"
CODIGO_BONUS = "VIP2025"

# ---------------- START ---------------- #

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if users.get(user_id) == "LIBERADO":
        await update.message.reply_text(
            "✅ Você já tem acesso liberado.\n"
            f"Grupo: {LINK_GRUPO}"
        )
        return

    users[user_id] = "AGUARDANDO_PAGAMENTO"

    await update.message.reply_text(
        f"🔥 RESERVA ATIVADA\n\n"
        f"💰 VIP: {VALOR}\n"
        f"🔑 Pix: {PIX}\n\n"
        "⚠️ Após pagar envie o comprovante aqui."
    )

# ---------------- MENSAGENS ---------------- #

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    status = users.get(user_id)

    if status == "AGUARDANDO_PAGAMENTO":
        await update.message.reply_text(
            "⏳ Estamos aguardando o pagamento.\n"
            "Assim que o Pix for identificado, seu acesso será liberado."
        )

    elif status == "LIBERADO":
        await update.message.reply_text(
            "✅ Seu acesso já foi liberado.\n"
            f"Grupo: {LINK_GRUPO}"
        )

    else:
        await update.message.reply_text(
            "Digite /start para iniciar."
        )

# ---------------- CONFIRMAÇÃO MANUAL ---------------- #

async def confirmar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
