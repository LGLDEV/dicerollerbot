import disnake
from disnake.ext import commands

import config


words = ['fuck', 'jeal up']

# setup client
intents = disnake.Intents(messages = True, message_content=True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix=".", intents=intents)
client.remove_command('help')




@client.event 
async def on_ready():
	print(f"Bot {client.user} is ready to work")

@client.event
async def on_message(message):
	for word in words:
		if word in message.content:
			await message.delete()
			await message.channel.send(f"{message.author.mention} bu so'zlarni ishlatish mumkin emas")
 


if __name__ == '__main__':
	client.run(config.settings['TOKEN'])
