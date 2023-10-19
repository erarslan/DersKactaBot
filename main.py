import pdf
from telegram import Update
from telegram.ext import CommandHandler, Updater

my_token = open('token.txt', 'r').read()

TOKEN = my_token

def start(update: Update, context):
    user = update.effective_user
    update.message.reply_html(f"Selam {user.mention_html()}! Ders programını öğrenmek için <i>/gün</i> yazabilirsin.")

def gun (update:Update, context):
    update.message.reply_html("Lütfen günü direkt giriniz, örnek kullanım: <i>/pazartesi</i>, <i>/sali</i>...")

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
    dp.add_handler(CommandHandler('gun', gun))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()