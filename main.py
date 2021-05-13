import discord 
import json
from datetime import datetime
from fetchdata import FetchData
from discord_bot import MyClient

def getrownumber(hour,date):
    row=(hour//2)+3+(12 if date%2==0 else 0)
    return row

time = datetime.today()
hour = time.hour
date = time.day
row = getrownumber(hour,date)
data = FetchData()
Responders = data.getdata(RANGE='C'+str(row))
Verifiers = data.getdata(RANGE='D'+str(row))
Researchers = data.getdata(RANGE='E'+str(row))
Responders_List=str(Responders[0][0]).split(',')
Verifiers_List=str(Verifiers[0][0]).split(',')
Researchers_List=str(Researchers[0][0]).split(',')
token=""
with open('discord-token.json','r') as file:
    for data in file:
        token+=data
token = json.loads(token)
intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
client.run(token["client-secret"])