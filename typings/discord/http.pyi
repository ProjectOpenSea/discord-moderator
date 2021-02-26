"""
This type stub file was generated by pyright.
"""

import logging

"""
The MIT License (MIT)

Copyright (c) 2015-2020 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
log = logging.getLogger(__name__)
async def json_or_text(response):
    ...

class Route:
    BASE = ...
    def __init__(self, method, path, **parameters) -> None:
        ...
    
    @property
    def bucket(self):
        ...
    


class MaybeUnlock:
    def __init__(self, lock) -> None:
        ...
    
    def __enter__(self):
        ...
    
    def defer(self):
        ...
    
    def __exit__(self, type, value, traceback):
        ...
    


class HTTPClient:
    """Represents an HTTP client sending HTTP requests to the Discord API."""
    SUCCESS_LOG = ...
    REQUEST_LOG = ...
    def __init__(self, connector=..., *, proxy=..., proxy_auth=..., loop=..., unsync_clock=...) -> None:
        ...
    
    def recreate(self):
        ...
    
    async def ws_connect(self, url, *, compress=...):
        ...
    
    async def request(self, route, *, files=..., **kwargs):
        ...
    
    async def get_from_cdn(self, url):
        ...
    
    async def close(self):
        ...
    
    async def static_login(self, token, *, bot):
        ...
    
    def logout(self):
        ...
    
    def start_group(self, user_id, recipients):
        ...
    
    def leave_group(self, channel_id):
        ...
    
    def add_group_recipient(self, channel_id, user_id):
        ...
    
    def remove_group_recipient(self, channel_id, user_id):
        ...
    
    def edit_group(self, channel_id, **options):
        ...
    
    def convert_group(self, channel_id):
        ...
    
    def start_private_message(self, user_id):
        ...
    
    def send_message(self, channel_id, content, *, tts=..., embed=..., nonce=..., allowed_mentions=..., message_reference=...):
        ...
    
    def send_typing(self, channel_id):
        ...
    
    def send_files(self, channel_id, *, files, content=..., tts=..., embed=..., nonce=..., allowed_mentions=..., message_reference=...):
        ...
    
    async def ack_message(self, channel_id, message_id):
        ...
    
    def ack_guild(self, guild_id):
        ...
    
    def delete_message(self, channel_id, message_id, *, reason=...):
        ...
    
    def delete_messages(self, channel_id, message_ids, *, reason=...):
        ...
    
    def edit_message(self, channel_id, message_id, **fields):
        ...
    
    def add_reaction(self, channel_id, message_id, emoji):
        ...
    
    def remove_reaction(self, channel_id, message_id, emoji, member_id):
        ...
    
    def remove_own_reaction(self, channel_id, message_id, emoji):
        ...
    
    def get_reaction_users(self, channel_id, message_id, emoji, limit, after=...):
        ...
    
    def clear_reactions(self, channel_id, message_id):
        ...
    
    def clear_single_reaction(self, channel_id, message_id, emoji):
        ...
    
    def get_message(self, channel_id, message_id):
        ...
    
    def get_channel(self, channel_id):
        ...
    
    def logs_from(self, channel_id, limit, before=..., after=..., around=...):
        ...
    
    def publish_message(self, channel_id, message_id):
        ...
    
    def pin_message(self, channel_id, message_id, reason=...):
        ...
    
    def unpin_message(self, channel_id, message_id, reason=...):
        ...
    
    def pins_from(self, channel_id):
        ...
    
    def kick(self, user_id, guild_id, reason=...):
        ...
    
    def ban(self, user_id, guild_id, delete_message_days=..., reason=...):
        ...
    
    def unban(self, user_id, guild_id, *, reason=...):
        ...
    
    def guild_voice_state(self, user_id, guild_id, *, mute=..., deafen=..., reason=...):
        ...
    
    def edit_profile(self, password, username, avatar, **fields):
        ...
    
    def change_my_nickname(self, guild_id, nickname, *, reason=...):
        ...
    
    def change_nickname(self, guild_id, user_id, nickname, *, reason=...):
        ...
    
    def edit_member(self, guild_id, user_id, *, reason=..., **fields):
        ...
    
    def edit_channel(self, channel_id, *, reason=..., **options):
        ...
    
    def bulk_channel_update(self, guild_id, data, *, reason=...):
        ...
    
    def create_channel(self, guild_id, channel_type, *, reason=..., **options):
        ...
    
    def delete_channel(self, channel_id, *, reason=...):
        ...
    
    def create_webhook(self, channel_id, *, name, avatar=..., reason=...):
        ...
    
    def channel_webhooks(self, channel_id):
        ...
    
    def guild_webhooks(self, guild_id):
        ...
    
    def get_webhook(self, webhook_id):
        ...
    
    def follow_webhook(self, channel_id, webhook_channel_id, reason=...):
        ...
    
    def get_guilds(self, limit, before=..., after=...):
        ...
    
    def leave_guild(self, guild_id):
        ...
    
    def get_guild(self, guild_id):
        ...
    
    def delete_guild(self, guild_id):
        ...
    
    def create_guild(self, name, region, icon):
        ...
    
    def edit_guild(self, guild_id, *, reason=..., **fields):
        ...
    
    def get_template(self, code):
        ...
    
    def create_from_template(self, code, name, region, icon):
        ...
    
    def get_bans(self, guild_id):
        ...
    
    def get_ban(self, user_id, guild_id):
        ...
    
    def get_vanity_code(self, guild_id):
        ...
    
    def change_vanity_code(self, guild_id, code, *, reason=...):
        ...
    
    def get_all_guild_channels(self, guild_id):
        ...
    
    def get_members(self, guild_id, limit, after):
        ...
    
    def get_member(self, guild_id, member_id):
        ...
    
    def prune_members(self, guild_id, days, compute_prune_count, roles, *, reason=...):
        ...
    
    def estimate_pruned_members(self, guild_id, days):
        ...
    
    def get_all_custom_emojis(self, guild_id):
        ...
    
    def get_custom_emoji(self, guild_id, emoji_id):
        ...
    
    def create_custom_emoji(self, guild_id, name, image, *, roles=..., reason=...):
        ...
    
    def delete_custom_emoji(self, guild_id, emoji_id, *, reason=...):
        ...
    
    def edit_custom_emoji(self, guild_id, emoji_id, *, name, roles=..., reason=...):
        ...
    
    def get_all_integrations(self, guild_id):
        ...
    
    def create_integration(self, guild_id, type, id):
        ...
    
    def edit_integration(self, guild_id, integration_id, **payload):
        ...
    
    def sync_integration(self, guild_id, integration_id):
        ...
    
    def delete_integration(self, guild_id, integration_id):
        ...
    
    def get_audit_logs(self, guild_id, limit=..., before=..., after=..., user_id=..., action_type=...):
        ...
    
    def get_widget(self, guild_id):
        ...
    
    def create_invite(self, channel_id, *, reason=..., **options):
        ...
    
    def get_invite(self, invite_id, *, with_counts=...):
        ...
    
    def invites_from(self, guild_id):
        ...
    
    def invites_from_channel(self, channel_id):
        ...
    
    def delete_invite(self, invite_id, *, reason=...):
        ...
    
    def get_roles(self, guild_id):
        ...
    
    def edit_role(self, guild_id, role_id, *, reason=..., **fields):
        ...
    
    def delete_role(self, guild_id, role_id, *, reason=...):
        ...
    
    def replace_roles(self, user_id, guild_id, role_ids, *, reason=...):
        ...
    
    def create_role(self, guild_id, *, reason=..., **fields):
        ...
    
    def move_role_position(self, guild_id, positions, *, reason=...):
        ...
    
    def add_role(self, guild_id, user_id, role_id, *, reason=...):
        ...
    
    def remove_role(self, guild_id, user_id, role_id, *, reason=...):
        ...
    
    def edit_channel_permissions(self, channel_id, target, allow, deny, type, *, reason=...):
        ...
    
    def delete_channel_permissions(self, channel_id, target, *, reason=...):
        ...
    
    def move_member(self, user_id, guild_id, channel_id, *, reason=...):
        ...
    
    def remove_relationship(self, user_id):
        ...
    
    def add_relationship(self, user_id, type=...):
        ...
    
    def send_friend_request(self, username, discriminator):
        ...
    
    def application_info(self):
        ...
    
    async def get_gateway(self, *, encoding=..., v=..., zlib=...):
        ...
    
    async def get_bot_gateway(self, *, encoding=..., v=..., zlib=...):
        ...
    
    def get_user(self, user_id):
        ...
    
    def get_user_profile(self, user_id):
        ...
    
    def get_mutual_friends(self, user_id):
        ...
    
    def change_hypesquad_house(self, house_id):
        ...
    
    def leave_hypesquad_house(self):
        ...
    
    def edit_settings(self, **payload):
        ...
    

