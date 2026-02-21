elif texto == "✅ Já Paguei":

    await update.message.reply_text(
        f"""📩 ENVIO DE COMPROVANTE

Entre no grupo abaixo e envie seu comprovante:

{GRUPO_COMPROVANTE}

⚠️ IMPORTANTE:
• O nome do comprovante deve ser o mesmo do Telegram.
• Após confirmação manual, você receberá o link do VIP.
• Pagamentos falsos serão ignorados.

Aguarde a validação.
"""
    )
