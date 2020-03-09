import discord


f = open("keys.txt", "r")
TOKEN = f.readline().strip()
serverID= int(f.readline().strip())

print(TOKEN)
print(serverID)
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(TOKEN)