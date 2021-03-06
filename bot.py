import argparse
import asyncio
from asyncio.tasks import Task
import os
import re
import shlex
from datetime import timedelta
from typing import List, NoReturn, Optional, Set, cast

import discord
from discord.abc import Messageable
from discord.member import Member
from discord.message import Message


BOT_TOKEN = os.getenv('BOT_TOKEN')
CONFIRMATION = 'iknowwhatiamdoing'

client = discord.Client()


class AutoMessage:
    def __init__(self, *, channel: Messageable, content: str, interval: Optional[timedelta]=None, keywords: Optional[Set[str]]=None, task: Optional[Task[NoReturn]]=None):
        self.channel = channel
        self.content = content
        self.interval = interval
        self.keywords = keywords
        self.task = task


auto_messages: List[AutoMessage] = []


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
        or not message.content
        or member == client.user
    ):
        return

    if (
        not is_admin(member)
        or not message.content.startswith('!')
    ):
        for auto_message in auto_messages:
            if auto_message.keywords and any(re.search(f"\\b{keyword}\\b", message.content) for keyword in auto_message.keywords):
                await auto_message.channel.send(auto_message.content)
        return

    try:
        [command, *arguments] = shlex.split(message.content.strip())
    except ValueError:
        [command, *arguments] = message.content.strip().split()

    parser = None
    try:
        if command == '!ban-all':
            parser = argparse.ArgumentParser(prog="!ban-all", description='Ban all users matching a given name.', add_help=False)
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

        if command == '!message':
            parser = argparse.ArgumentParser(prog="!message", description='Automatically send messages.', add_help=False)
            parser.add_argument('message', nargs="+", help='the content of the message')
            parser.add_argument('--channel', required=True, help='the channel into which the message will be posted')
            parser.add_argument('--keywords', help='comma-separated list of keywords to respond to')
            parser.add_argument('--seconds', type=int, default=0, help='period in seconds')
            parser.add_argument('--minutes', type=int, default=0, help='period in minutes')
            parser.add_argument('--hours', type=int, default=0, help='period in hours')
            parser.add_argument('--days', type=int, default=0, help='period in days')
            args = vars(parser.parse_args(arguments))
            content: str = " ".join(args["message"])
            channel_name: str = args["channel"]
            keywords: Optional[Set[str]] = args["keywords"] and set(args["keywords"].split(","))
            tdelta = timedelta(seconds=args["seconds"], minutes=args["minutes"], hours=args["hours"], days=args["days"])
            duration = tdelta.total_seconds()
            channel = None
            for c in guild.channels:
                if c.name == channel_name:
                    channel = cast(Messageable, c)
            if not channel:
                await message.channel.send(f'No such channel found: {channel_name}')
                return
            if keywords:
                auto_messages.append(AutoMessage(channel=channel, content=content, keywords=keywords))
                await message.channel.send(f'Message set to automatically respond to these keywords: {", ".join(keywords)}')
                return
            await channel.send(content)
            await message.channel.send(f'Sent message to {channel_name}.')
            if duration > 0:
                async def run():
                    while True:
                        await asyncio.sleep(duration)
                        if channel:
                            await channel.send(content)
                loop = asyncio.get_event_loop()
                task = loop.create_task(run())
                auto_messages.append(AutoMessage(channel=channel, content=content, interval=tdelta, task=task))
                await message.channel.send(f'Will also send message to {channel_name} every {tdelta}.')

        if command == '!manage-messages':
            parser = argparse.ArgumentParser(prog="!manage-messages", description='Manage automatic messages.', add_help=False)
            parser.add_argument('--list', action="store_true", help='list all messages')
            parser.add_argument('--delete', type=int, help='which message to delete')
            args = vars(parser.parse_args(arguments))
            is_list = args["list"]
            delete_id = args["delete"]
            if is_list:
                list_str = "\n".join(f"({i}) #{am.channel} [every {am.interval or 'n/a'}] [keywords: {am.keywords or 'n/a'}]: {am.content}" for i, am in enumerate(auto_messages))
                await message.channel.send(f"Currently stored messages:\n{list_str}")
                return
            if delete_id is not None:
                auto_message = auto_messages.pop(delete_id)
                if auto_message.task:
                    auto_message.task.cancel()
                await message.channel.send(f'Deleted message ({delete_id}).')
                return
            await message.channel.send(parser.format_help())

        else:
            await message.channel.send(f'Unrecognized command: {command}')

    except Exception as error:
        print(error)
        await message.channel.send(f'Error: {error}')
    except:
        if parser:
            await message.channel.send(parser.format_help())
        pass


client.run(BOT_TOKEN)
