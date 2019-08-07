from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
trainer = ListTrainer(bot)

for files in os.listdir(os.path.abspath('yml')):
    data = open(os.path.abspath('yml') + "/" + files, 'r').readlines()
    trainer.train(data)


while True:
    menssagem = input("Você: ")
    resposta = bot.get_response(menssagem)
    print("Bot: ",resposta)
