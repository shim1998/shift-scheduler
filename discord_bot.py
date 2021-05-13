import discord
import json

class MyClient(discord.Client):

    async def on_ready(self):
        self.members=[]
        print('Logged on as {0}!'.format(self.user))
        for guild in self.guilds:
            data = list(guild.members)
            for x in data:
                print(x.name,x.id,x.nick)
                self.members.append([x.name,x.id,x.nick])


    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        channel = message.channel
        if message.content.startswith('hello'):
            await channel.send("Sup {0.author}: {0.content}".format(message))
        if message.content.startswith('tag everyone'):
            for spam in self.members:
                await channel.send("HI <@"+str(spam[1])+">")

token=""
with open('discord-token.json','r') as file:
    for data in file:
        token+=data
token = json.loads(token)
intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
client.run(token["client-secret"])