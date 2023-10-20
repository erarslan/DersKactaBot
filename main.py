import pdf
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Updater, CallbackQueryHandler

my_token = open('token.txt', 'r').read()

TOKEN = my_token

def start(update: Update, context):
    anaklavye = [
        [InlineKeyboardButton("1. Sınıf", callback_data="sınıf_1")],
        [InlineKeyboardButton("2. Sınıf", callback_data="sınıf_2")],
        [InlineKeyboardButton("3. Sınıf", callback_data="sınıf_3")]
    ]
    reply_markup = InlineKeyboardMarkup(anaklavye)
    user = update.effective_user
    update.message.reply_html(f"Selam! {user.mention_html()}! Lütfen aşağıdan sınıfını seç:", reply_markup=reply_markup)



def isle(update: Update, context):
    query = update.callback_query

    if query.data.startswith("sınıf"):
        sayi = query.data.split('_')[1]
        alt_butonlar = [
                [InlineKeyboardButton("Pazartesi", callback_data=f'pazartesi_{sayi}')],
                [InlineKeyboardButton("Salı", callback_data=f'sali_{sayi}')],
                [InlineKeyboardButton("Çarşamba", callback_data=f'carsamba_{sayi}')],
                [InlineKeyboardButton("Perşembe", callback_data=f'persembe_{sayi}')],
                [InlineKeyboardButton("Cuma", callback_data=f'cuma_{sayi}')]
                ]
        reply_markup = InlineKeyboardMarkup(alt_butonlar)
        query.edit_message_text("Lütfen aşağıdan gün seç:", reply_markup=reply_markup)
    
    else:
        sayi = query.data.split('_')[1]
        if query.data.startswith("pazartesi"):
            query.edit_message_text(pdf.createProgram("Pazartesi", sayi))
        elif query.data.startswith("sali"):
            query.edit_message_text(pdf.createProgram("Sali", sayi))
        elif query.data.startswith("carsamba"):
            query.edit_message_text(pdf.createProgram("Carsamba", sayi))
        elif query.data.startswith("persembe"):
            query.edit_message_text(pdf.createProgram("Persembe", sayi))
        elif query.data.startswith("cuma"):
            query.edit_message_text(pdf.createProgram("Cuma", sayi))

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(isle))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()