import pdf
from telegram import Update
from telegram.ext import CommandHandler, Updater

TOKEN = '6340995753:AAGe5LAanKMhVTGaYIID0fJnnzT3qqRhzz4'

def start(update: Update, context):
    user = update.effective_user
    update.message.reply_html(f"Selam {user.mention_html()}! Ders programını öğrenmek için <i>/gün</i> yazabilirsin.")

def send(update: Update, context, day):
    update.message.reply_html(pdf.createProgram(day))

def pazartesi(update: Update, context):
    send(update, context, 'Pazartesi')

def sali(update: Update, context):
    send(update, context, 'Sali')

def carsamba(update: Update, context):
    send(update, context, 'Carsamba')

def persembe(update: Update, context):
    send(update, context, 'Persembe')

def cuma(update: Update, context):
    send(update, context, 'Cuma')

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('pazartesi', pazartesi))
    dp.add_handler(CommandHandler('sali', sali))
    dp.add_handler(CommandHandler('carsamba', carsamba))
    dp.add_handler(CommandHandler('persembe', persembe))
    dp.add_handler(CommandHandler('cuma', cuma))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()