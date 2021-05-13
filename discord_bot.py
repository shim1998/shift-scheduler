import discord
import json

class MyClient(discord.Client):

    async def on_ready(self):
        self.members=[]
        self.channels=[]
        for guild in self.guilds:
            for channel in guild.channels:
                pass
                # print(channel.id,channel.name)
        for guild in self.guilds:
            data = list(guild.members)
            for x in data:
                # print(x.name,x.id,x.nick)
                self.members.append([x.name,x.id,x.nick])
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        channel = message.channel
        channel.id = 840581432660852746
        if message.content.startswith('hello'):
            await channel.send("Sup {0.author}: {0.content}".format(message))
        if message.content.startswith('tag everyone'):
            for spam in self.members:
                await channel.send("HI <@"+str(spam[1])+">")