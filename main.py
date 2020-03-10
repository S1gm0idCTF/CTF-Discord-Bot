import discord
from discord.ext import commands

f = open("keys.txt", "r")
TOKEN = f.readline().strip()
serverID = int(f.readline().strip())

###############################################################################################
#####################################  Variables  #############################################
###############################################################################################

bot = commands.Bot(command_prefix='!')
class CTF():
	def __init__(self):
		self.activeCTF = ""
	def setCTF(self, ctfname):
		self.activeCTF = ctfname
	def getCTF(self):
		return self.activeCTF
	
activeCTF = CTF()
@bot.event
async def on_ready():
	global activeCTF
	
@bot.event
async def on_message(message):
	print("Message from {0.author}: {0.content} in channel: {0.channel}".format(message))
	await bot.process_commands(message)

###############################################################################################
#####################################  COMMANDS  ##############################################
###############################################################################################
@bot.command()
async def currentctf(ctx):
	if activeCTF.getCTF() == "":
		await ctx.send("Please run `!setctf [ctfname]` or `!ctf [ctfname]`first.")
	else:
		await ctx.send("`{}`, is the selected CTF.".format(activeCTF.getCTF()))
	pass
@bot.command()
async def setctf(ctx, ctfname):
	category = discord.utils.get(ctx.guild.categories, name=ctfname.lower())
	print(category)
	if category != None:
		activeCTF.setCTF(ctfname)
	else:
		await ctx.send("That ctf doesn't exist :'(")
	pass
@bot.command()
async def ctf(ctx, *ctfname):
	ctfname = '_'.join(ctfname)
	if not discord.utils.get(ctx.guild.categories, name=ctfname):
		await ctx.guild.create_category(ctfname.lower())
		activeCTF.setCTF(ctfname.lower())
	pass
@bot.command()
async def q(ctx, *questionTitle):
	if activeCTF.getCTF() == "":
		await ctx.send("Please run `!setctf [ctfname]` or `!ctf [ctfname]`first.")
	else:
		questionTitle = '_'.join(questionTitle).lower()
		category = discord.utils.get(ctx.guild.categories, name=activeCTF.getCTF())
		await ctx.guild.create_text_channel(questionTitle, category=category)
	pass
@bot.command()
async def merge(ctx, category):
	category = discord.utils.get(ctx.guild.categories, name=category)
	ctx.guild.create_text_channel("__archive", category=category)
	file = ""
	for textChannel in category.channels:
		file = file + "\n# " + str(category.name) + ": " + str(textChannel.name)
		if str(textChannel.type) == "text" and str(textChannel.name) != "__archive":
			messages = await textChannel.history().flatten()
			m = [x.content for x in messages][::-1] #reverse messages
			for i in m:
				file = file + "\n" + " - " + i 
		file = file + "\n---"
	ctx.guild.create_text_channel("archive", category=category)
	await ctx.send(file)
	pass
###############################################################################################

bot.run(TOKEN)
