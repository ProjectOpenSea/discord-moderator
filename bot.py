import asyncio
import os
from typing import Callable, Dict, List, Optional, Tuple

import discord
from discord.member import Member
from discord.message import Message


BOT_TOKEN = os.getenv('BOT_TOKEN')
CONFIRMATION = 'iknowwhatiamdoing'

client = discord.Client()

auto_messages: Dict[str, Callable[..., None]] = {}


def is_admin(member: Member) -> bool:
    return any(role.permissions.administrator for role in member.roles)


def parse(message: Message) -> Tuple[str, Optional[List[str]]]:
    words = message.content.strip().split()
    return words[0], words[1:]


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
        or not message.content.startswith("!")
        or member == client.user
    ):
        return

    command, arguments = parse(message)

    if command == '!ban-all':
        if not arguments:
            return
        name_to_match = arguments[0]
        matched_members = [m for m in guild.members if m.name == name_to_match]
        if len(arguments) == 2 and arguments[1] == CONFIRMATION:
            await asyncio.gather(*[guild.ban(m, delete_message_days=7) for m in matched_members])
            await message.channel.send(f'Banned {len(matched_members)} user(s).')
        else:
            await message.channel.send(f'Would ban {len(matched_members)} user(s).')


client.run(BOT_TOKEN)
