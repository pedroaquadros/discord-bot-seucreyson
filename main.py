import discord

TOKEN = 'NTUzMjM2NTg1NzM5NzE0NTYw.D2MxLQ.dzohlo96rV9WZpVO9WAJ8ag7nUo'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!picks'):
        msg = 'https://imgur.com/a/i4Ru5m9'
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)