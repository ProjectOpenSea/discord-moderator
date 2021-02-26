"""
This type stub file was generated by pyright.
"""

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
class EnumMeta(type):
    def __new__(cls, name, bases, attrs):
        ...
    
    def __iter__(cls):
        ...
    
    def __reversed__(cls):
        ...
    
    def __len__(cls):
        ...
    
    def __repr__(cls):
        ...
    
    @property
    def __members__(cls):
        ...
    
    def __call__(cls, value):
        ...
    
    def __getitem__(cls, key):
        ...
    
    def __setattr__(cls, name, value):
        ...
    
    def __delattr__(cls, attr):
        ...
    
    def __instancecheck__(self, instance):
        ...
    


class Enum(metaclass=EnumMeta):
    @classmethod
    def try_value(cls, value):
        ...
    


class ChannelType(Enum):
    text = ...
    private = ...
    voice = ...
    group = ...
    category = ...
    news = ...
    store = ...
    def __str__(self) -> str:
        ...
    


class MessageType(Enum):
    default = ...
    recipient_add = ...
    recipient_remove = ...
    call = ...
    channel_name_change = ...
    channel_icon_change = ...
    pins_add = ...
    new_member = ...
    premium_guild_subscription = ...
    premium_guild_tier_1 = ...
    premium_guild_tier_2 = ...
    premium_guild_tier_3 = ...
    channel_follow_add = ...


class VoiceRegion(Enum):
    us_west = ...
    us_east = ...
    us_south = ...
    us_central = ...
    eu_west = ...
    eu_central = ...
    singapore = ...
    london = ...
    sydney = ...
    amsterdam = ...
    frankfurt = ...
    brazil = ...
    hongkong = ...
    russia = ...
    japan = ...
    southafrica = ...
    south_korea = ...
    india = ...
    europe = ...
    dubai = ...
    vip_us_east = ...
    vip_us_west = ...
    vip_amsterdam = ...
    def __str__(self) -> str:
        ...
    


class SpeakingState(Enum):
    none = ...
    voice = ...
    soundshare = ...
    priority = ...
    def __str__(self) -> str:
        ...
    
    def __int__(self) -> int:
        ...
    


class VerificationLevel(Enum):
    none = ...
    low = ...
    medium = ...
    high = ...
    table_flip = ...
    extreme = ...
    double_table_flip = ...
    very_high = ...
    def __str__(self) -> str:
        ...
    


class ContentFilter(Enum):
    disabled = ...
    no_role = ...
    all_members = ...
    def __str__(self) -> str:
        ...
    


class UserContentFilter(Enum):
    disabled = ...
    friends = ...
    all_messages = ...


class FriendFlags(Enum):
    noone = ...
    mutual_guilds = ...
    mutual_friends = ...
    guild_and_friends = ...
    everyone = ...


class Theme(Enum):
    light = ...
    dark = ...


class Status(Enum):
    online = ...
    offline = ...
    idle = ...
    dnd = ...
    do_not_disturb = ...
    invisible = ...
    def __str__(self) -> str:
        ...
    


class DefaultAvatar(Enum):
    blurple = ...
    grey = ...
    gray = ...
    green = ...
    orange = ...
    red = ...
    def __str__(self) -> str:
        ...
    


class RelationshipType(Enum):
    friend = ...
    blocked = ...
    incoming_request = ...
    outgoing_request = ...


class NotificationLevel(Enum):
    all_messages = ...
    only_mentions = ...


class AuditLogActionCategory(Enum):
    create = ...
    delete = ...
    update = ...


class AuditLogAction(Enum):
    guild_update = ...
    channel_create = ...
    channel_update = ...
    channel_delete = ...
    overwrite_create = ...
    overwrite_update = ...
    overwrite_delete = ...
    kick = ...
    member_prune = ...
    ban = ...
    unban = ...
    member_update = ...
    member_role_update = ...
    member_move = ...
    member_disconnect = ...
    bot_add = ...
    role_create = ...
    role_update = ...
    role_delete = ...
    invite_create = ...
    invite_update = ...
    invite_delete = ...
    webhook_create = ...
    webhook_update = ...
    webhook_delete = ...
    emoji_create = ...
    emoji_update = ...
    emoji_delete = ...
    message_delete = ...
    message_bulk_delete = ...
    message_pin = ...
    message_unpin = ...
    integration_create = ...
    integration_update = ...
    integration_delete = ...
    @property
    def category(self):
        ...
    
    @property
    def target_type(self):
        ...
    


class UserFlags(Enum):
    staff = ...
    partner = ...
    hypesquad = ...
    bug_hunter = ...
    mfa_sms = ...
    premium_promo_dismissed = ...
    hypesquad_bravery = ...
    hypesquad_brilliance = ...
    hypesquad_balance = ...
    early_supporter = ...
    team_user = ...
    system = ...
    has_unread_urgent_messages = ...
    bug_hunter_level_2 = ...
    verified_bot = ...
    verified_bot_developer = ...


class ActivityType(Enum):
    unknown = ...
    playing = ...
    streaming = ...
    listening = ...
    watching = ...
    custom = ...
    competing = ...
    def __int__(self) -> int:
        ...
    


class HypeSquadHouse(Enum):
    bravery = ...
    brilliance = ...
    balance = ...


class PremiumType(Enum):
    nitro_classic = ...
    nitro = ...


class TeamMembershipState(Enum):
    invited = ...
    accepted = ...


class WebhookType(Enum):
    incoming = ...
    channel_follower = ...


class ExpireBehaviour(Enum):
    remove_role = ...
    kick = ...


ExpireBehavior = ExpireBehaviour
class StickerType(Enum):
    png = ...
    apng = ...
    lottie = ...


def try_enum(cls, val):
    """A function that tries to turn the value into enum ``cls``.

    If it fails it returns the value instead.
    """
    ...

