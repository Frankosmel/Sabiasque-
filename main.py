
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN, ADMIN_ID
from handlers.admin import setup_admin_handlers
from handlers.publish import setup_publish_handlers
from handlers.channel import setup_channel_handlers
from utils.scheduler import start_scheduler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("🚫 No estás autorizado para usar este bot.")
        return
    keyboard = ReplyKeyboardMarkup([
        ["📤 Publicar ahora", "🕓 Programar publicación"],
        ["📚 Ver programadas", "🗑️ Eliminar programadas"],
        ["📡 Canales", "🛑 Cancelar acción"],
        ["/comandos"]
    ], resize_keyboard=True)
    await update.message.reply_text("👋 ¡Bienvenido administrador!
Selecciona una opción del menú 👇", reply_markup=keyboard)

async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📖 *Comandos disponibles:*
"
        "• /start – Iniciar el bot
"
        "• /comandos – Mostrar este menú
"
        "• 📤 Publicar ahora – Enviar imagen + texto
"
        "• 🕓 Programar publicación – Agendar contenido
"
        "• 📚 Ver programadas – Mostrar publicaciones agendadas
"
        "• 🗑️ Eliminar programadas – Eliminar publicaciones futuras
"
        "• 📡 Canales – Administrar canales
"
        "• 🛑 Cancelar acción – Detener el flujo actual
"
        f"
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹"
    )
    await update.message.reply_markdown(text)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("comandos", comandos))

    setup_admin_handlers(app)
    setup_publish_handlers(app)
    setup_channel_handlers(app)

    start_scheduler(app)
    print("✅ Bot funcionando.")
    app.run_polling()

if __name__ == "__main__":
    main()
