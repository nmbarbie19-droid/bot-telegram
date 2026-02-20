user_id = update.effective_user.id
estado = usuarios.get(user_id)

if estado == "aguardando_pagamento":
    await context.bot.send_message(
        chat_id=user_id,
        text="⏳ Seu acesso ainda está disponível.\nQuer garantir antes que o valor aumente?"
    )
