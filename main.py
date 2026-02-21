from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8323335001:AAFv3yD7Gy1DDFUB4kWPPBcyISc7V2bheOc
"

VALOR = "R$19,99"
CHAVE_PIX = "11948212565"

GRUPO_COMPROVANTE = "https://t.me/+ZqnMDshtQ6k4OTBh"
GRUPO_PREVIAS = "https://t.me/+ETimjCvSzUc4YWZh"


# ===== INICIO =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """🔥 ACESSO VIP PRIVADO 🔥

Conteúdo exclusivo 🔥
Material reservado 😈

Se quiser participar digite:

quero participar

Ou digite:

ver previas"""
    )


# ===== MENSAGENS =====
async def mensagens(update: Update, context: ContextTypes.DEFAULT_TYPE):

    texto = update.message.text.lower()

    # ===== QUERO PARTICIPAR =====
    if texto in ["quero participar", "eu quero", "manda sim", "quero"]:

        await update.message.reply_text(
            f"""💎 ACESSO VIP 💎

Valor do acesso: {VALOR}

Pagamento via PIX 👇

Chave PIX:
{CHAVE_PIX}

Após pagar digite:

ja paguei"""
        )

    # ===== JA PAGUEI =====
    elif texto in ["ja paguei", "paguei", "enviei pix"]:

        await update.message.reply_text(
            f"""📩 ENVIO DO COMPROVANTE

Entre no grupo abaixo e envie seu comprovante:

{GRUPO_COMPROVANTE}

Após validação manual você receberá o link VIP."""
        )

    # ===== PREVIAS =====
    elif texto in ["ver previas", "previas", "quero ver"]:

        await update.message.reply_text(
            f"""👀 PRÉVIAS DISPONÍVEIS

Acesse aqui:
{GRUPO_PREVIAS}

Quando quiser o VIP digite:

quero participar"""
        )

    # ===== QUALQUER OUTRA COISA =====
    else:
        await update.message.reply_text(
            "Digite: quero participar  ou  ver previas"
        )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensagens))

print("BOT ONLINE 🚀")

app.run_polling()
