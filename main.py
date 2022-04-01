import discord

client = discord.Client()

@client.event

async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Welcome to Dev_Hub! {member.name}, We are happy to have you here. Please, State your name and what you do. I am Compli_Bot, the official Dev_Hub bot, I was created by members of the Dev_Hub Community. I will be happy to help you with whatever you need. Just in case you need me, find me in the BOTS category.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$Hey Alexa"):
        await message.channel.send(f"Hi {message.author} ")




client.run("OTU5MzE4NDc3ODg0MjMxNzAx.YkaI9A.SBN-lO6NweZA-RiGN9RmfyySaUU")