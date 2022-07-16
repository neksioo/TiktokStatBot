import discord
import requests
import time
import json
import os

from fake_headers import Headers
from discord.ext import tasks
from discord.ext import commands


with open('config.json') as f:
        config = json.load(f)

token = config.get('token')

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')
intents = discord.Intents.all()

@bot.event
async def on_ready():
    print('Ready')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name='.tt | neksio.gq'))

@bot.command(aliases=['tiktok', 'tik'])
async def tt(ctx, user):
    username = ctx.message.author.name
    avataruser = ctx.author.avatar_url
    if '@' in user:
        user = user.replace('@', '')
    if f'https://www.tiktok.com/@' or 'https://tiktok.com/@' or 'https://www.tiktok.vm/@' or 'https://tiktok.vm/@' in user:
        product = user
        if product == 'https://www.tiktok.com/@':
            user = user.replace('https://www.tiktok.com/@', '')
        elif product == 'https://tiktok.com/@':
            user = user.replace('https://tiktok.com/@', '')
        elif product == 'https://www.tiktok.vm/@':
            user = user.replace('https://www.tiktok.vm/@', '')
        elif product == 'https://tiktok.vm/@':
            user = user.replace('https://tiktok.vm/@', '')
        async with ctx.typing():
            header = Headers(
                headers=False
            )
            for i in range(1):
                followers = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['stats']['followerCount']
            for i in range(1):
                following = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['stats']['followingCount']
            for i in range(1):
                avatar = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['user']['avatarLarger']
            for i in range(1):
                signature = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['user']['signature']
            for i in range(1):
                videos = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['stats']['videoCount']
            for i in range(1):
                hearts = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['stats']['heart']
            for i in range(1):
                unique = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['user']['uniqueId']
            for i in range(1):
                id = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['user']['id']
            for i in range(1):
                nick = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['user']['nickname']

                embed=discord.Embed(title=f'@{unique}', url=f'https://tiktok.com/@{unique}', description=f'{signature}', color=0xddb3c4)
                embed.set_author(name=f'{username}', icon_url=f'{avataruser}')
                embed.set_thumbnail(url=f'{avatar}')
                embed.add_field(name='**Name**', value=f'{nick}', inline=False)
                embed.add_field(name='**Posts**', value=f'{videos}', inline=False)
                embed.add_field(name='**Hearts**', value=f'{hearts}', inline=True)
                embed.add_field(name='**Followers**', value=f'{followers}', inline=True)
                embed.add_field(name='**Following**', value=f'{following}', inline=True)
                embed.set_footer(text=f'🆔 {id}')
                await ctx.send(embed=embed)
    else:
            async with ctx.typing():
                header = Headers(
                    headers=False
                )
                for i in range(1):
                    followers = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['stats']['followerCount']
                for i in range(1):
                    following = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['stats']['followingCount']
                for i in range(1):
                    avatar = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['user']['avatarLarger']
                for i in range(1):
                    signature = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['user']['signature']
                for i in range(1):
                    videos = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['stats']['videoCount']
                for i in range(1):
                    hearts = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['stats']['heart']
                for i in range(1):
                    unique = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['user']['uniqueId']
                for i in range(1):
                    id = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['user']['id']
                for i in range(1):
                    nick = requests.get(f'https://www.tiktok.com/node/share/user/@{user}?aid=1988', headers=header.generate()).json()['userInfo']['user']['nickname']

                embed1=discord.Embed(title=f'@{unique}', url=f'https://tiktok.com/@{unique}', description=f'{signature}', color=0xddb3c4)
                embed1.set_author(name=f'{username}', icon_url=f'{avataruser}')
                embed1.set_thumbnail(url=f'{avatar}')
                embed1.add_field(name='**Name**', value=f'{nick}', inline=False)
                embed1.add_field(name='**Posts**', value=f'{videos}', inline=False)
                embed1.add_field(name='**Hearts**', value=f'{hearts}', inline=True)
                embed1.add_field(name='**Followers**', value=f'{followers}', inline=True)
                embed1.add_field(name='**Following**', value=f'{following}', inline=True)
                embed1.set_footer(text=f'🆔 {id}')
                await ctx.send(embed=embed1)


if __name__ == '__main__':
    bot.run(token)
