from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import asyncio
import os

TOKEN = os.getenv("TOKEN")

usuarios = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    usuarios[user_id] = "inicio"

    await update.message.reply_text(
        "🔥 Acesso VIP+18😈 disponível hoje.\n"
        "Conteúdo exclusivo +18.\n\n"
        "Quer garantir agora?\n"
        "Responde: SIM ou NAO"
    )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    texto = update.message.text.lower()
    estado = usuarios.get(user_id)

    if estado == "inicio" and "sim" in texto:
        usuarios[user_id] = "aguardando_pagamento"

        await update.message.reply_text(
            "💎 Perfeito.\n"
            "Hoje está R$19,99.\n\n"
            "💸 Pague aqui:\n"
            "CHAVE PIX 11948212565\n\n"
            "Depois envie: PAGUEI"
        )

        asyncio.create_task(followup(update, context))
        return

    if estado == "inicio" and "nao" in texto:
        usuarios[user_id] = "encerrado"
        await update.message.reply_text(
            "Sem problemas 👍\n"
            "Se mudar de ideia, volte aqui."
        )
        return

    if estado == "aguardando_pagamento" and "paguei" in texto:
        usuarios[user_id] = "acesso_liberado"

        await update.message.reply_text(
            "🔥 Pagamento recebido.\n"
            "Aqui está seu acesso VIP:\n"
            "https://t.me/+ETimjCvSzUc4YWZh\n\n"
            "Bem-vindo 😈"
        )
        return

    await update.message.reply_text("OBRIGADA PELO CONTATO! 💋")

async def followup(update, context):
    await asyncio.sleep(600)

    user_id = update.effective_user.id
    estado = usuarios.get(user_id)

    if estado == "aguardando_pagamento":
        await context.bot.send_message(
            chat_id=user_id,
            text="⏳ Seu acesso ainda está disponível.\nQuer garantir antes que o valor aumente?"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.run_polling()

if __name__ == "__main__":
    main()
