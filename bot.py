from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

conversa = ['oi', 'olá', 'olá, bom dia', 'bom dia', 'bom dia, como vai?', 'estou bem']
conversa2 = ['qual é o seu filme favorito', 'o meu filme favorito é truque de mestre']
bot.set_trainer(ListTrainer)
bot.train(conversa)
bot.train(conversa2)

while True:
  quest = input('Você: ')
  response = bot.get_response(quest)
  print('Bot: ', response)