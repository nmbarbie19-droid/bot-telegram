from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ================= CONFIG ================= #

TOKEN = "8323335001:AAFv3yD7Gy1DDFUB4kWPPBcyISc7V2bheOc"
VALOR = "R$19,99"
PIX = "11948212565"
LINK_GRUPO = "https://t.me/SEU_GRUPO"
CODIGO_BONUS = "VIP2025"

# ================= BANCO SIMPLES ================= #

users = {}

# ================= START ================= #

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if users.get(user_id) == "LIBERADO":
        await update.message.reply_text(
            f"✅ Você já tem acesso.\n\n👉 {LINK_GRUPO}"
        )
        return

    users[user_id] = "AGUARDANDO_PAGAMENTO"

    await update.message.reply_text(
        f"🔥 RESERVA ATIVADA\n\n"
        f"💰 Valor VIP: {VALOR}\n"
        f"🔑 Chave Pix: {PIX}\n\n"
        "⚠️ Após pagar, envie qualquer mensagem aqui.\n"
        "Assim que o Pix cair, liberamos seu acesso."
    )

# ================= MENSAGENS ================= #

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    status = users.get(user_id)

    if status == "AGUARDANDO_PAGAMENTO":
        await update.message.reply_text(
            "⏳ Estamos aguardando a confirmação do pagamento.\n"
            "Assim que o Pix for identificado, o acesso será liberado."
        )

    elif status == "LIBERADO":
        await update.message.reply_text(
            f"✅ Seu acesso já está liberado.\n\n👉 {LINK_GRUPO}"
        )

    else:
        await update.message.reply_text(
            "Digite /start para iniciar."
        )

# ================= CONFIRMAR PAGAMENTO ================= #

async def confirmar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args if context.args else []

    if not args:
        await update.message.reply_text(
            "Use assim:\n/confirmar ID_DO_USUARIO"
        )
        return

    try:
        user_id = int(args[0])
    except ValueError:
        await update.message.reply_text("ID inválido.")
        return

    users[user_id] = "LIBERADO"

    await context.bot.send_message(
        chat_id=user_id,
        text=(
            "✅ PAGAMENTO CONFIRMADO!\n\n"
            f"🎁 Código bônus: {CODIGO_BONUS}\n\n"
            f"👉 Acesse o grupo agora:\n{LINK_GRUPO}\n\n"
            "⚠️ O conteúdo fixado é o principal. Salve agora."
        )
    )

    await update.message.reply_text("Usuário liberado com sucesso.")

# ================= MAIN ================= #

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("confirmar", confirmar))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot rodando igual máquina de fazer dinheiro 💸🔥")
    app.run_polling()

if __name__ == "__main__":
    main()
