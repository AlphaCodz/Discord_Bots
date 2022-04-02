from turtle import color, title
import discord


client = discord.Client()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_member_join(member):
    channel = client.get_channel(942415645872631860)
    await channel.send(f'{member} Welcome to Dev_Hub!  I am ALEXA, the current Bot for Dev_Hub Please state you name and what you in this format \
        name: "My name" \
        profession: "e.g i can write codes in python, js, or i am a copyrighter e.t.c".')
    
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$Hey Alexa"):
        await message.channel.send(f"Hi {message.author} ")

    if message.content.startswith ("Alexa's Current Version"):
        
        myEmbed = discord.Embed(title = "Current Version", description = "Version 1.0", color=0x00ff00)
        myEmbed.add_field(name= "Version Code", value = "AlexAv 1.0.1", inline=False)
        myEmbed.add_field(name= "Date Released", value = "8:04:022 [April 1st, 2022]", inline=False)
        myEmbed.set_footer(text="dev_hub")
        myEmbed.set_author(name= f"{message.author}")
        
        await message.channel.send(embed=myEmbed)
        
@client.event
async def on_disconnect():
    general_channel = client.get_channel(942415645872631860)
    await general_channel.send("Alexa Shutting Down!")
    
      
@client.event
async def on_member_remove(member):
  channel = client.get_channel(942415645872631860)
  await channel.send(f'{member} has left a server.')


client.run("")