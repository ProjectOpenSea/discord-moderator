import argparse
import asyncio
import os
import shlex
from typing import Callable, Dict, cast

import discord
from discord.abc import Messageable
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

    [command, *arguments] = shlex.split(message.content.strip())

    try:
        if command == '!ban-all':
            parser = argparse.ArgumentParser(description='Ban all users matching a given name.')
            parser.add_argument('name', help='the name to match')
            parser.add_argument(f"--{CONFIRMATION}", action="store_true", help='actually execute the bans')
            args = vars(parser.parse_args(arguments))
            name: str = args["name"]
            is_confirmed: bool = args[CONFIRMATION]
            matched_members = [m for m in guild.members if m.name == name]
            if is_confirmed:
                await message.channel.send(f'Banning {len(matched_members)} user(s)...')
                await asyncio.gather(*[guild.ban(m, delete_message_days=7) for m in matched_members])
                await message.channel.send(f'Banned {len(matched_members)} user(s).')
            else:
                await message.channel.send(f'Would ban {len(matched_members)} user(s).')

        if command == '!automessage':
            parser = argparse.ArgumentParser(description='Automatically post messages.')
            parser.add_argument('message', nargs="+", help='the content of the message')
            parser.add_argument('--channel', required=True, help='the channel into which the message will be posted')
            args = vars(parser.parse_args(arguments))
            channel_name: str = args["channel"]
            content: str = " ".join(args["message"])
            for channel in guild.channels:
                if channel.name == channel_name:
                    await cast(Messageable, channel).send(content)
                    return
            await message.channel.send(f'No such channel found: {channel_name}')

    except:
        pass


client.run(BOT_TOKEN)
