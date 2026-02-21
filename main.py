import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("8323335001:AAFv3yD7Gy1DDFUB4kWPPBcyISc7V2bheOc")

usuarios = {}

VALOR_VIP = "R$ 19,99"
CHAVE_PIX = "11948212565"

LINK_GRUPO_CONFIRMACAO = "https://t.me/+ZqnMDshtQ6k4OTBh"
LINK_GRUPO_PREVIA = "https://t.me/+ETimjCvSzUc4YWZh"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    usuarios[user_id] = {"estado": "inicio"}

    await update.message.reply_text(
        "🔥 ACESSO VIP🔞 DISPONÍVEL\n\n"
        "Digite QUERO para gerar sua reserva."
    )


async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    texto = update.message.text.strip().lower()

    if user_id not in usuarios:
        usuarios[user_id] = {"estado": "inicio"}

    estado = usuarios[user_id]["estado"]

    # GERA RESERVA
    if estado == "inicio" and "quero" in texto:
        usuarios[user_id]["estado"] = "aguardando"

        await update.message.reply_text(
            "🔥 RESERVA GERADA\n\n"
            f"💰 Valor: {VALOR_VIP}\n\n"
            "🔑 Chave Pix:\n"
            f"{CHAVE_PIX}\n\n"
            "⏳ Expira em 5 minutos.\n\n"
            "Após pagar, envie qualquer mensagem aqui."
        )

        asyncio.create_task(expirar(context, user_id))

    # CONFIRMA PAGAMENTO (simples)
    elif estado == "aguardando":
        usuarios[user_id]["estado"] = "confirmado"

        await update.message.reply_text(
            "✅ Pagamento confirmado.\n\n"
            "Entre no grupo de confirmação:\n\n"
            f"{LINK_GRUPO_CONFIRMACAO}"
        )

    # SE ESTÁ NA PRÉVIA E QUER TENTAR DE NOVO
    elif estado == "expirado" and "quero" in texto:
        usuarios[user_id]["estado"] = "aguardando"

        await update.message.reply_text(
            "🔥 Nova reserva gerada\n\n"
            f"💰 Valor: {VALOR_VIP}\n\n"
            "🔑 Chave Pix:\n"
            f"{CHAVE_PIX}\n\n"
            "⏳ Expira em 5 minutos."
        )

        asyncio.create_task(expirar(context, user_id))

    elif estado == "expirado":
        await update.message.reply_text(
            "Você está no grupo de prévia.\n\n"
            "Digite QUERO para tentar novamente."
        )


async def expirar(context: ContextTypes.DEFAULT_TYPE, user_id: int):
    await asyncio.sleep(300)

    if user_id in usuarios and usuarios[user_id]["estado"] == "aguardando":
        usuarios[user_id]["estado"] = "expirado"

        await context.bot.send_message(
            chat_id=user_id,
            text=(
                "⏰ Tempo encerrado.\n\n"
                "Entre no grupo de prévia:\n\n"
                f"{LINK_GRUPO_PREVIA}\n\n"
                "Lá você pode voltar para o bot quando quiser."
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
