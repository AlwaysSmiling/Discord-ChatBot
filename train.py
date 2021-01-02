from main import smilingnovelbot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer

trainer = ChatterBotCorpusTrainer(smilingnovelbot)
trainer.train("chatterbot.corpus.english.botprofile","chatterbot.corpus.english.conversations")

file = open("data_list.txt", "r", encoding='utf-8')
datastr = file.read()
file.close()
data_list = datastr.split('&-&')

trainer1 = ListTrainer(smilingnovelbot)


file1 = open("data_list1.txt", "r", encoding='utf-8')
datastr1 = file1.read()
file1.close()
data_list1 = datastr1.split('&-&')

trainer2 = ListTrainer(smilingnovelbot)
trainer2.train(data_list1)

file2 = open("data_lis.txt", "r", encoding='utf-8')
datastr2 = file2.read()
file2.close()
data_list2 = datastr2.split('&-&')

trainer3 = ListTrainer(smilingnovelbot)
trainer3.train(data_list2)
trainer1.train(data_list)