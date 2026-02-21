from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8323335001:AAFv3yD7Gy1DDFUB4kWPPBcyISc7V2bheOc"

VALOR = "R$19,99"
CHAVE_PIX = "11948212565"

GRUPO_COMPROVANTE = "https://t.me/SEU_GRUPO_COMPROVANTES"
GRUPO_PREVIAS = "https://t.me/SEU_GRUPO_PREVIAS"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["🔥 Quero Acesso VIP"],
        ["👀 Ver Prévias"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        """🔥 ACESSO VIP EXCLUSIVO 🔥

Conteúdo privado + atualizações frequentes.

Escolha uma opção abaixo 👇""",
        reply_markup=reply_markup
    )


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
            f"""💎 ACESSO VIP 💎

Valor promocional: {VALOR}

Pagamento via PIX 👇

🔑 Chave PIX:
{CHAVE_PIX}

⚠️ Após realizar o pagamento, clique em:
✅ Já Paguei""",
            reply_markup=reply_markup
        )

    # ===== JÁ PAGUEI =====
    elif texto == "✅ Já Paguei":

        keyboard = [["⬅️ Voltar ao Menu"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        await update.message.reply_text(
            f"""📩 ENVIO DE COMPROVANTE

Entre no grupo
