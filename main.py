import discord
from discord.ext import commands



f = open("keys.txt", "r")
TOKEN = f.readline().strip()
serverID = int(f.readline().strip())

print(TOKEN)
print(serverID)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	print("Logged on as")
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.event
async def on_message(message):
	print(message)
	print("Message from {0.author}: {0.content} in channel: {0.channel}".format(message))

	await bot.process_commands(message)

@bot.command()
async def test(ctx):
	print("hi")


bot.run(TOKEN)
