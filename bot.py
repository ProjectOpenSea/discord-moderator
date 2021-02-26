import argparse
import asyncio
import os
from typing import Callable, Dict

import discord
from discord.member import Member
from discord.message import Message


BOT_TOKEN = os.getenv('BOT_TOKEN')
CONFIRMATION = 'iknowwhatiamdoing'

client = discord.Client()

auto_messages: Dict[str, Callable[..., None]] = {}


def is_admin(member: Member) -> bool:
    return any(role.permissions.administrator for role in member.roles)


@client.event
async def on_ready() -> None:
    print(f'We have logged in as {client.user}.')


@client.event
async def on_message(message: Message) -> None:
    guild = message.guild
    member = message.author

    if (
        not guild
        or not isinstance(member, Member)
        or not is_admin(member)
        or not message.content
        or not message.content.startswith('!')
        or member == client.user
    ):
        return

    [command, *arguments] = message.content.strip().split()

    try:
        if command == '!ban-all':
            parser = argparse.ArgumentParser(description='Ban all users matching a given name.')
            parser.add_argument('name', help='the name to match')
            parser.add_argument(f"--{CONFIRMATION}", action="store_true", help='actually execute the bans')
            args = vars(parser.parse_args(arguments))
            matched_members = [m for m in guild.members if m.name == args["name"]]
            if args[CONFIRMATION]:
                await message.channel.send(f'Banning {len(matched_members)} user(s)...')
                await asyncio.gather(*[guild.ban(m, delete_message_days=7) for m in matched_members])
                await message.channel.send(f'Banned {len(matched_members)} user(s).')
            else:
                await message.channel.send(f'Would ban {len(matched_members)} user(s).')

        if command == '!auto-message':
            pass
    except Exception as error:
        print(error)


client.run(BOT_TOKEN)
