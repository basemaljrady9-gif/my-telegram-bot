import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "9279782162:AAETLGkf4LUmSzqRgH8jPjrXl8BxoqbtJRk"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً فيك! أنا بوتك شغال ✅\nارسل أي رسالة وأنا برد عليك.")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"وصلتني رسالتك: {update.message.text}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
