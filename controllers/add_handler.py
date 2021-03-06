import Database
import telepot

# Messages
USAGE_MESSAGE = "Usage: `/add <user> <amount>` to add a someone who owes you $$$"
USER_NOT_FOUND = "Either specified user does not exist or is currently not using the bot. Please request for him/her to add @paybobbot"

def add_handler(user_id, arguments):
    # Initialize bot and database helpers
    paybot = telepot.Bot("452146569:AAH0sXMgA9rtZe7j83L6RqqLU0qbo0sY12w")
    db = Database.Database()

    # Handle add
    try:
        if (len(arguments) < 3):
            paybot.sendMessage(user_id, USAGE_MESSAGE)
        else:
            payer = db.getUsername(user_id)
            payee = arguments[0]
            amount = arguments[1]
            description = arguments[2]
            if (db.getChatID(payee) == None):
                paybot.sendMessage(user_id, USER_NOT_FOUND)
            elif(float(amount) > 0):
                paybot.sendMessage(user_id, "Successfully added receipt:\nLoaned ${} to {}".format(amount, payee))
                db.addReceipt(payer, payee, description, amount)
            else:
                paybot.sendMessage(user_id, USAGE_MESSAGE)
    except:
        paybot.sendMessage(user_id, USAGE_MESSAGE)
