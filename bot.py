import json
import discord
import os 

intents = discord.Intents().all()
client = discord.Client(intents=intents)
server_id = 123 # YOUR_SERVER_ID
        

@client.event
async def on_ready():
    server = client.get_guild(server_id)  # YOUR_SERVER_ID

    members = server.members
    member_count = len(members)
    online_count = len([m for m in members if m.status != discord.Status.offline])

    data = {
        'member_count': member_count,
        'online_count': online_count,
        'members': [str(m) for m in members]
    }

    with open('server_data.json', 'w') as f:
        json.dump(data, f)
      
      
if client.is_closed():
    print("The bot is disconnected")
else:
    print("The bot is connected")

@client.event
async def on_disconnect():
    await client.close()

client.run('token') #token
