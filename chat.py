from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import random

bot = ChatBot('Luíza')
trainer = ListTrainer(bot)

for files in os.listdir(os.path.abspath('Conversations')):
    data = open(os.path.abspath('Conversations') + "/" + files, 'r').readlines()
    trainer.train(data)
    
    
while True:
    message = input("You: ")
    numberOfMessages = random.randint(1,4)
    previousMessage = ""
    response = ""
    for x in range(numberOfMessages):
        while response == previousMessage:
            response = bot.get_response(message)
        print("Bot: ",response)
        previousMessage = response
