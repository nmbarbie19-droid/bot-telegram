from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import asyncio
import os
import random

TOKEN = os.getenv("TOKEN")

usuarios = {}

def gerar_codigo():
    return f"VIP{random.randint(1000,9999)}"

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    usuarios[user_id] = {"estado": "inicio"}

    await update.message.reply_text(
        "🔥 ACESSO VIP +18 LIBERADO HOJE 🔥\n\n"
        "Conteúdo exclusivo 🔞\n"
        "Atualizações diárias 😈\n\n"
        "⚠️ Vagas limitadas.\n\n"
        "Quer garantir agora?\n"
        "Responda: SIM ou NAO"
    )

# RESPOSTAS
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    texto = update.message.text.upper()

    if user_id not in usuarios:
        return

    dados = usuarios[user_id]
    estado = dados["estado"]

    # QUER COMPRAR
    if estado == "inicio" and "SIM" in texto:
        codigo = gerar_codigo()

        usuarios[user_id] = {
            "estado": "aguardando_pagamento",
            "codigo": codigo
        }

        await update.message.reply_text(
            f"💎 Perfeito!\n\n"
            f"Valor hoje: R$19,99\n\n"
            f"💸 PIX: 11948212565\n\n"
            f"🧾 Seu código exclusivo:\n{codigo}\n\n"
            f"Envie após pagar:\nPAGUEI {codigo}\n\n"
            f"⚠️ Liberação imediata após validação."
        )

        asyncio.create_task(followup(user_id, context))
        return

    # NÃO QUER
    if estado == "inicio" and "NAO" in texto:
        usuarios[user_id]["estado"] = "encerrado"

        await update.message.reply_text(
            "Sem problemas 👍\n\n"
            "Se mudar de ideia, volte aqui.\n"
            "Mas aviso: o valor pode subir."
        )
        return

    # CONFIRMA PAGAMENTO
    if estado == "aguardando_pagamento":
        codigo = dados["codigo"]

        if "PAGUEI" in texto and codigo in texto:
            usuarios[user_id]["estado"] = "acesso_liberado"

            await update.message.reply_text(
                "🔥 Pagamento confirmado!\n\n"
                "Aqui está seu acesso VIP:\n"
                "https://t.me/+ETimjCvSzUc4YWZh\n\n"
                "Bem-vindo(a) 😈"
            )
            return

    await update.message.reply_text("Digite corretamente 👍")

# FOLLOW-UP AUTOMÁTICO
async def followup(user_id, context):
    await asyncio.sleep(600)

    dados = usuarios.get(user_id)

    if dados and dados["estado"] == "aguardando_pagamento":
        await context.bot.send_message(
            chat_id=user_id,
            text="⏳ Seu acesso ainda está reservado.\n"
                 "Quer garantir antes que o valor aumente?"
        )

# MAIN
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.run_polling()

if __name__ == "__main__":
    main()
