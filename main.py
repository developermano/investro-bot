import logging

from telegram import Bot,InlineKeyboardButton, InlineKeyboardMarkup, ReplyMarkup, Update, ReplyKeyboardMarkup, KeyboardButton, keyboardbutton, user
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)



token = "5742271194:AAGHrWdm9RFHbfzdkibjLikabMHx2uc5y_c"
bot=Bot(token)
admin_id=2039990859


def start(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id==admin_id:
        msg='''
        welcome to investro bot
        '''
        update.message.reply_text(msg)




def text(update: Update, context: CallbackContext) -> None:    
    msg=update.message.text
    try:
        matchname=msg[msg.index("private contest for ")+20:msg.index("Spots: ")].rstrip()
        entry=msg[msg.index("Entry: ")+7:msg.index("Spots: ")].rstrip()
        spots=msg[msg.index("Spots: ")+7:msg.index("1st Prize: ")].rstrip()
        istprize=msg[msg.index("1st Prize: ")+11:msg.index("Deadline: ")].rstrip()
        link=msg[msg.index("-Tap ")+5:msg.index("-Use contest code")].rstrip()
        mymsg='''
contest type : {}
entry fee : {}
spots     : {}
1st prize : {}
        '''
        mymsgfinal=mymsg.format(matchname,entry,spots,istprize)
        keyboard=[[InlineKeyboardButton("join contest",url=link)]]
        reply_markup=InlineKeyboardMarkup(keyboard)
        update.message.reply_text(mymsgfinal,reply_markup=reply_markup,quote=False)
        update.message.delete()
    except:
        update.message.delete()


def main() -> None:
    """Run the bot."""
    updater = Updater(token)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(
        Filters.text & ~ Filters.command,text))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()