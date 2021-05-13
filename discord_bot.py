import asyncio
import discord
import json

from fetch import Fetch

class MyClient(discord.Client):

    async def on_ready(self):
        self.members=[]
        self.required_members=[]
        for guild in self.guilds:
            for channel in guild.channels:
                pass
                # print(channel.id,channel.name)
        for guild in self.guilds:
            data = guild.members
            for x in data:
                # print(x.name,x.id,x.nick)
                self.members.append([x.name,x.id,x.nick])
        print('Logged on as {0}!'.format(self.user))
        # await asyncio.sleep(60 * 50 * 2)
        self.members_to_ping = Fetch().return_data()
        print(self.members_to_ping)
        self.ids,self.members_to_tag=[],[]
        for member in self.members:
            if member[2] in self.members_to_ping:
                self.ids.append(member[1])
                self.members_to_tag.append(member[2])

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        channel = message.channel
        channel.id = 840581432660852746
        print(self.ids)
        print(self.members_to_tag)
        if message.content.startswith('hello'):
            await channel.send("Sup {0.author}: {0.content}".format(message))
        if message.content.startswith('tag everyone'):
            for spam in self.members:
                await channel.send("HI <@{0}>".format(spam[1]))

token=""
with open('discord-token.json','r') as file:
    for data in file:
        token+=data
token = json.loads(token)
intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
client.run(token["client-secret"])