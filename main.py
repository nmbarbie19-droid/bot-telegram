import os
import random
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")

usuarios = {}

def gerar_codigo():
    return f"VIP{random.randint(1000,9999)}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    usuarios[user_id] = {"estado": "inicio"}

    await update.message.reply_text(
        "⚠️ Acesso VIP por 18 hoje.\n\n"
        "Digite 1 para garantir.\n"
        "Digite 2 para sair."
    )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    texto = update.message.text.lower()

    if user_id not in usuarios:
        usuarios[user_id] = {"estado": "inicio"}

    estado = usuarios[user_id]["estado"]

    if estado == "inicio":
        if texto == "1":
            codigo = gerar_codigo()
            usuarios[user_id]["estado"] = "aguardando"

            await update.message.reply_text(
                f"🔥 Código: {codigo}\n"
                "Faça o Pix de 18 e envie comprovante.\n"
                "Expira em 30 minutos."
            )

            asyncio.create_task(lembrete(context, user_id))

        else:
            await update.message.reply_text("Ok. Quando quiser, me chama.")

async def lembrete(context, user_id):
    await asyncio.sleep(1200)
    if user_id in usuarios and usuarios[user_id]["estado"] == "aguardando":
        await context.bot.send_message(
            chat_id=user_id,
            text="⏳ Último aviso antes de expirar."
        )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
