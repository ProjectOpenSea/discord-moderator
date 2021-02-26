import argparse
import asyncio
from asyncio.tasks import Task
import os
import shlex
from datetime import timedelta
from typing import Dict, NoReturn, cast

import discord
from discord.abc import Messageable
from discord.member import Member
from discord.message import Message


BOT_TOKEN = os.getenv('BOT_TOKEN')
CONFIRMATION = 'iknowwhatiamdoing'

client = discord.Client()

automessages: Dict[str, Task[NoReturn]] = {}


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
            parser = argparse.ArgumentParser(prog="!ban-all", description='Ban all users matching a given name.')
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
            parser = argparse.ArgumentParser(prog="!message", description='Automatically post messages.')
            parser.add_argument('message', nargs="+", help='the content of the message')
            parser.add_argument('--channel', required=True, help='the channel into which the message will be posted')
            parser.add_argument('--seconds', type=int, default=0, help='period in seconds')
            parser.add_argument('--minutes', type=int, default=0, help='period in minutes')
            parser.add_argument('--hours', type=int, default=0, help='period in hours')
            parser.add_argument('--days', type=int, default=0, help='period in days')
            args = vars(parser.parse_args(arguments))
            channel_name: str = args["channel"]
            content: str = " ".join(args["message"])
            duration = timedelta(seconds=args["seconds"], minutes=args["minutes"], hours=args["hours"], days=args["days"]).total_seconds()
            for channel in guild.channels:
                if channel.name == channel_name:
                    await cast(Messageable, channel).send(content)
                    if duration > 0:
                        async def run():
                            while True:
                                await asyncio.sleep(duration)
                                await cast(Messageable, channel).send(content)
                        loop = asyncio.get_event_loop()
                        task = loop.create_task(run())
                        automessages[content] = task
                    return
            await message.channel.send(f'No such channel found: {channel_name}')

        if command == '!manage-messages':
            parser = argparse.ArgumentParser(prog="!manage-messages", description='Manage automatic messages.')
            parser.add_argument('--delete', type=int, help='the content of the message')
            args = vars(parser.parse_args(arguments))
            delete_id = args["delete"]
            if delete_id is not None:
                automessages.pop(list(automessages)[delete_id]).cancel()
            else:
                for i, msg in enumerate(automessages):
                    await message.channel.send(f"{i}: {msg}")

        else:
            await message.channel.send(f'Unrecognized command: {command}')

    except Exception as error:
        print(error)
        await message.channel.send(f'Error: {error}')
    except:
        pass


client.run(BOT_TOKEN)
