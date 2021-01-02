import discord
from chatterbot import ChatBot

smilingnovelbot = ChatBot(name='SmilingNovel',storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///db.sqlite3',read_only=True, logic_adapters=["chatterbot.logic.BestMatch"])


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.channel.id == 794199373008338974:
            await message.channel.send(smilingnovelbot.get_response(message.content))

def run():
    client = MyClient()
    client.run('TOKEN')