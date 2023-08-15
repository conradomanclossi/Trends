import os
import discord
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Intents
intents = discord.Intents.default()
intents.members = True

# Create a Discord client
client = discord.Client(intents=intents)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: {user_message} ({channel})')

        await message.channel.send('Hello!')

# Event handler for when a message is sent
client.run(token)