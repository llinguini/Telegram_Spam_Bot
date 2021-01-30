import botogram
bot = botogram.create("AQUI VA EL TOKEN DEL BOT")
bot.owner = "linguini"

@bot.command("spam")
def spam_command(chat, message, args):
	
    for i in range (10000):
        chat.send("*PON TU MENSAJE AQUI*")
       

if __name__ == "__main__":
    bot.run()
