import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("8323335001:AAFv3yD7Gy1DDFUB4kWPPBcyISc7V2bheOc")

usuarios = {}

VALOR_VIP = "R$ 19,99"
CHAVE_PIX = "11948212565"

LINK_GRUPO_VIP = "https://t.me/+ZqnMDshtQ6k4OTBh"
LINK_GRUPO_PREVIA = "https://t.me/+ETimjCvSzUc4YWZh"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    usuarios[user_id] = {"estado": "inicio"}

    await update.message.reply_text(
        "🔥 ACESSO VIP DISPONÍVEL\n\n"
        "Conteúdo exclusivo + grupo fechado.\n\n"
        "Digite EU QUERO para garantir agora."
    )


async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    texto = update.message.text.strip().lower()

    if user_id not in usuarios:
        usuarios[user_id] = {"estado": "inicio"}

    estado = usuarios[user_id]["estado"]

    # GERA RESERVA (aceita qualquer frase com 'quero')
    if estado == "inicio" and "quero" in texto:
        usuarios[user_id]["estado"] = "aguardando"

        await update.message.reply_text(
            "🔥 RESERVA ATIVADA\n\n"
            f"💰 Valor: {VALOR_VIP}\n\n"
            "🔑 Chave Pix:\n"
            f"{CHAVE_PIX}\n\n"
            "⏳ Expira em 5 minutos.\n\n"
            "Após pagar, envie qualquer mensagem aqui."
        )

        asyncio.create_task(expirar(context, user_id))

    # CONFIRMAÇÃO SIMPLES
    elif estado == "aguardando":
        usuarios[user_id]["estado"] = "vip"

        await update.message.reply_text(
            "✅ Pagamento confirmado!\n\n"
            "🔓 Acesso liberado:\n\n"
            f"{LINK_GRUPO_VIP}"
        )

    # SE JÁ EXPIROU
    elif estado == "expirado":
        await update.message.reply_text(
            "⏰ Sua reserva expirou.\n\n"
            "Grupo de prévia:\n"
            f"{LINK_GRUPO_PREVIA}\n\n"
            "Digite EU QUERO para tentar novamente."
        )


async def expirar(context: ContextTypes.DEFAULT_TYPE, user_id: int):
    await asyncio.sleep(300)

    if user_id in usuarios and usuarios[user_id]["estado"] == "aguardando":
        usuarios[user_id]["estado"] = "expirado"

        await context.bot.send_message(
            chat_id=user_id,
            text=(
                "⏰ Tempo encerrado.\n\n"
                "Você foi direcionado para o grupo de prévia:\n\n"
                f"{LINK_GRUPO_PREVIA}"
            )
        )


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("Bot rodando...")
    app.run_polling()


if __name__ == "__main__":
    main()
