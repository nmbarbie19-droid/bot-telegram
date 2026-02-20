import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")

usuarios = {}

VALOR_VIP = "R$ 19,99"
CHAVE_PIX = "11948212565"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    usuarios[user_id] = {"estado": "inicio"}

    await update.message.reply_text(
        "🔥 ACESSO VIP 🔞 DISPONÍVEL HOJE\n\n"
        "• Conteúdo exclusivo 😈😜\n"
        "• Grupo secreto 🙈\n"
        "• Acesso imediato após confirmação\n\n"
        "⚠️ Vagas limitadas hoje\n\n"
        "Digite EU QUERO para garantir agora."
    )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    texto = update.message.text.strip().lower()

    if user_id not in usuarios:
        usuarios[user_id] = {"estado": "inicio"}

    estado = usuarios[user_id]["estado"]

    gatilhos = ["eu quero", "quero", "1", "sim"]

    if estado == "inicio" and texto in gatilhos:
        usuarios[user_id]["estado"] = "aguardando_pagamento"

        await update.message.reply_text(
            "🔥 RESERVA ATIVADA 🔥\n\n"
            f"💰 Valor do VIP: {VALOR_VIP}\n\n"
            "🔑 Chave Pix:\n"
            f"{CHAVE_PIX}\n\n"
            "⏳ Expira em 5 minutos.\n\n"
            "Após pagar, envie o comprovante aqui."
        )

        asyncio.create_task(expiracao(context, user_id))

    elif estado == "aguardando
