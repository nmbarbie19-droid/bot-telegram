from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ===== CONFIG =====
TOKEN = "8323335001:AAFv3yD7Gy1DDFUB4kWPPBcyISc7V2bheOc


"

VALOR = "R$19,99"
CHAVE_PIX = "11948212565"

GRUPO_COMPROVANTE = "https://t.me/+ZqnMDshtQ6k4OTBh"
GRUPO_PREVIAS = "https://t.me/+ETimjCvSzUc4YWZh"


# ===== MENU INICIAL =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["🔥 Quero Acesso VIP"],
        ["👀 Ver Prévias"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        """🔥 ACESSO VIP PRIVADO 🔥

Conteúdo exclusivo 🔥
Material que NÃO fica exposto 😈
Acesso reservado somente para membros.

Escolha uma opção abaixo 👇""",
        reply_markup=reply_markup
    )


# ===== RESPOSTAS =====
async def mensagens(update: Update, context: ContextTypes.DEFAULT_TYPE):

    texto = update.message.text

    # ===== QUERO VIP =====
    if texto == "🔥 Quero Acesso VIP":

        keyboard = [
            ["✅ Já Paguei"],
            ["⬅️ Voltar ao Menu"]
        ]

        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        await update.message.reply_text(
            f"""💎 ACESSO VIP LIBERADO 💎

🔥 Oferta ativa agora

💰 Valor do acesso: {VALOR}

Pagamento via PIX 👇

🔑 Chave PIX:
{CHAVE_PIX}

⚠️ Após realizar o pagamento clique em:
✅ Já Paguei""",
            reply_markup=reply_markup
        )

    # ===== JÁ PAGUEI =====
    elif texto == "✅ Já Paguei":

        keyboard = [["⬅️ Voltar ao Menu"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        await update.message.reply_text(
            f"""📩 ENVIO DO COMPROVANTE

Entre no grupo abaixo e envie seu comprovante:

{GRUPO_COMPROVANTE}

⚠️ IMPORTANTE:
• Nome do comprovante deve ser igual ao Telegram
• Pagamentos falsos serão ignorados
• Após validação manual você receberá o acesso VIP

Aguarde a confirmação 😉""",
            reply_markup=reply_markup
        )

    # ===== PRÉVIAS =====
    elif texto == "👀 Ver Prévias":

        keyboard = [["⬅️ Voltar ao Menu"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        await update.message.reply_text(
            f"""👀 PRÉVIAS LIBERADAS

Veja algumas prévias aqui 👇

{GRUPO_PREVIAS}

Quando quiser acesso completo 🔥
volte ao menu e clique em:

🔥 Quero Acesso VIP""",
            reply_markup=reply_markup
        )

    # ===== VOLTAR =====
    elif texto == "⬅️ Voltar ao Menu":
        await start(update, context)

    # ===== OUTROS TEXTOS =====
    else:
        await update.message.reply_text(
            "Use os botões do menu para continuar 👇"
        )


# ===== INICIAR BOT =====
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensagens))

print("BOT ONLINE 🚀")

app.run_polling()
