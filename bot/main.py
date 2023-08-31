import os
from dotenv import load_dotenv
import discord
from discord import app_commands
from langchain.llms import OpenAI

# Load the .env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild_id = os.getenv('DISCORD_GUILD')
openai_key = os.getenv('OPENAI_KEY')

class Client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = guild_id))
            self.synced = True
        print(f"Logged in as {self.user} (ID: {self.user.id}).")
        print("-----")

client = Client()
tree = app_commands.CommandTree(client)

@tree.command(name = "test", description = "testing", guild = discord.Object(id = guild_id))
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"Hello {name}! I was made with Discord.py!")

@tree.command(name="llm", description="Language Model", guild = discord.Object(id = guild_id))
async def self(interaction: discord.Interaction, prompt: str):
    llm = OpenAI(openai_api_key=openai_key, temperature=0.9)
    await interaction.response.send_message(llm.predict(prompt))

if __name__ == "__main__":
    client.run(token)
