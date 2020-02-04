import discord
from discord.ext import commands
from dotenv import load_dotenv
import random



# load_dotenv()
# token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '!')



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Guilds:\n')
    for guild in client.guilds:
    	print('\n --- ' + guild.name + '---\n')
    	members = '\n - '.join([member.name for member in guild.members])
    	print(f'Guild Members:\n - {members}')
    
    print('------')

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

	await client.process_commands(message)



@client.event
async def  on_member_join(member):
	print (f'{member} has joined a server')

@client.event
async def on_member_remove(member):
	print(f'{member} has left a server')

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}')

@client.command(aliases=['8ball'])
async def _8ball(ctx):
	responses = ['Бесспорно',
	'Предрешено',
	'Никаких сомнений',
	'Определённо да',
	'Можешь быть уверен в этом',
	'Мне кажется — «да»',
	'Вероятнее всего',
	'Хорошие перспективы',
	'Знаки говорят — «да»',
	'Пока не ясно, попробуй снова',
	'Спроси позже',
	'Лучше не рассказывать',
	'Сейчас нельзя предсказать',
	'Сконцентрируйся и спроси опять',
	'Даже не думай',
	'Мой ответ — «нет»',
	'По моим данным — «нет»',
	'Перспективы не очень хорошие',
	'Весьма сомнительно'
	]
	await ctx.send(f'Ответ: {random.choice(responses)}, {context.message.author.mention}')

client.run('Njc0MjcwNzY1NDQ4OTUzODY2.XjmJng.RcYsYGOtLEyXDwpdbbyJR44ege8')
