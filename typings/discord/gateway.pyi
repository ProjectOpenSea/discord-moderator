"""
This type stub file was generated by pyright.
"""

import logging
import threading
import aiohttp
from collections import namedtuple

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
class ReconnectWebSocket(Exception):
    """Signals to safely reconnect the websocket."""
    def __init__(self, shard_id, *, resume=...) -> None:
        ...
    


class WebSocketClosure(Exception):
    """An exception to make up for the fact that aiohttp doesn't signal closure."""
    ...


EventListener = namedtuple('EventListener', 'predicate event result future')
class GatewayRatelimiter:
    def __init__(self, count=..., per=...) -> None:
        ...
    
    def is_ratelimited(self):
        ...
    
    def get_delay(self):
        ...
    
    async def block(self):
        ...
    


class KeepAliveHandler(threading.Thread):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def run(self):
        ...
    
    def get_payload(self):
        ...
    
    def stop(self):
        ...
    
    def tick(self):
        ...
    
    def ack(self):
        ...
    


class VoiceKeepAliveHandler(KeepAliveHandler):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def get_payload(self):
        ...
    
    def ack(self):
        ...
    


class DiscordClientWebSocketResponse(aiohttp.ClientWebSocketResponse):
    async def close(self, *, code: int = ..., message: bytes = ...) -> bool:
        ...
    


class DiscordWebSocket:
    """Implements a WebSocket for Discord's gateway v6.

    Attributes
    -----------
    DISPATCH
        Receive only. Denotes an event to be sent to Discord, such as READY.
    HEARTBEAT
        When received tells Discord to keep the connection alive.
        When sent asks if your connection is currently alive.
    IDENTIFY
        Send only. Starts a new session.
    PRESENCE
        Send only. Updates your presence.
    VOICE_STATE
        Send only. Starts a new connection to a voice guild.
    VOICE_PING
        Send only. Checks ping time to a voice guild, do not use.
    RESUME
        Send only. Resumes an existing connection.
    RECONNECT
        Receive only. Tells the client to reconnect to a new gateway.
    REQUEST_MEMBERS
        Send only. Asks for the full member list of a guild.
    INVALIDATE_SESSION
        Receive only. Tells the client to optionally invalidate the session
        and IDENTIFY again.
    HELLO
        Receive only. Tells the client the heartbeat interval.
    HEARTBEAT_ACK
        Receive only. Confirms receiving of a heartbeat. Not having it implies
        a connection issue.
    GUILD_SYNC
        Send only. Requests a guild sync.
    gateway
        The gateway we are currently connected to.
    token
        The authentication token for discord.
    """
    DISPATCH = ...
    HEARTBEAT = ...
    IDENTIFY = ...
    PRESENCE = ...
    VOICE_STATE = ...
    VOICE_PING = ...
    RESUME = ...
    RECONNECT = ...
    REQUEST_MEMBERS = ...
    INVALIDATE_SESSION = ...
    HELLO = ...
    HEARTBEAT_ACK = ...
    GUILD_SYNC = ...
    def __init__(self, socket, *, loop) -> None:
        ...
    
    @property
    def open(self):
        ...
    
    def is_ratelimited(self):
        ...
    
    @classmethod
    async def from_client(cls, client, *, initial=..., gateway=..., shard_id=..., session=..., sequence=..., resume=...):
        """Creates a main websocket for Discord from a :class:`Client`.

        This is for internal use only.
        """
        ...
    
    def wait_for(self, event, predicate, result=...):
        """Waits for a DISPATCH'd event that meets the predicate.

        Parameters
        -----------
        event: :class:`str`
            The event name in all upper case to wait for.
        predicate
            A function that takes a data parameter to check for event
            properties. The data parameter is the 'd' key in the JSON message.
        result
            A function that takes the same data parameter and executes to send
            the result to the future. If ``None``, returns the data.

        Returns
        --------
        asyncio.Future
            A future to wait for.
        """
        ...
    
    async def identify(self):
        """Sends the IDENTIFY packet."""
        ...
    
    async def resume(self):
        """Sends the RESUME packet."""
        ...
    
    async def received_message(self, msg):
        ...
    
    @property
    def latency(self):
        """:class:`float`: Measures latency between a HEARTBEAT and a HEARTBEAT_ACK in seconds."""
        ...
    
    async def poll_event(self):
        """Polls for a DISPATCH event and handles the general gateway loop.

        Raises
        ------
        ConnectionClosed
            The websocket connection was terminated for unhandled reasons.
        """
        ...
    
    async def send(self, data):
        ...
    
    async def send_as_json(self, data):
        ...
    
    async def send_heartbeat(self, data):
        ...
    
    async def change_presence(self, *, activity=..., status=..., afk=..., since=...):
        ...
    
    async def request_sync(self, guild_ids):
        ...
    
    async def request_chunks(self, guild_id, query=..., *, limit, user_ids=..., presences=..., nonce=...):
        ...
    
    async def voice_state(self, guild_id, channel_id, self_mute=..., self_deaf=...):
        ...
    
    async def close(self, code=...):
        ...
    


class DiscordVoiceWebSocket:
    """Implements the websocket protocol for handling voice connections.

    Attributes
    -----------
    IDENTIFY
        Send only. Starts a new voice session.
    SELECT_PROTOCOL
        Send only. Tells discord what encryption mode and how to connect for voice.
    READY
        Receive only. Tells the websocket that the initial connection has completed.
    HEARTBEAT
        Send only. Keeps your websocket connection alive.
    SESSION_DESCRIPTION
        Receive only. Gives you the secret key required for voice.
    SPEAKING
        Send only. Notifies the client if you are currently speaking.
    HEARTBEAT_ACK
        Receive only. Tells you your heartbeat has been acknowledged.
    RESUME
        Sent only. Tells the client to resume its session.
    HELLO
        Receive only. Tells you that your websocket connection was acknowledged.
    RESUMED
        Sent only. Tells you that your RESUME request has succeeded.
    CLIENT_CONNECT
        Indicates a user has connected to voice.
    CLIENT_DISCONNECT
        Receive only.  Indicates a user has disconnected from voice.
    """
    IDENTIFY = ...
    SELECT_PROTOCOL = ...
    READY = ...
    HEARTBEAT = ...
    SESSION_DESCRIPTION = ...
    SPEAKING = ...
    HEARTBEAT_ACK = ...
    RESUME = ...
    HELLO = ...
    RESUMED = ...
    CLIENT_CONNECT = ...
    CLIENT_DISCONNECT = ...
    def __init__(self, socket, loop) -> None:
        ...
    
    async def send_as_json(self, data):
        ...
    
    send_heartbeat = ...
    async def resume(self):
        ...
    
    async def identify(self):
        ...
    
    @classmethod
    async def from_client(cls, client, *, resume=...):
        """Creates a voice websocket for the :class:`VoiceClient`."""
        ...
    
    async def select_protocol(self, ip, port, mode):
        ...
    
    async def client_connect(self):
        ...
    
    async def speak(self, state=...):
        ...
    
    async def received_message(self, msg):
        ...
    
    async def initial_connection(self, data):
        ...
    
    @property
    def latency(self):
        """:class:`float`: Latency between a HEARTBEAT and its HEARTBEAT_ACK in seconds."""
        ...
    
    @property
    def average_latency(self):
        """:class:`list`: Average of last 20 HEARTBEAT latencies."""
        ...
    
    async def load_secret_key(self, data):
        ...
    
    async def poll_event(self):
        ...
    
    async def close(self, code=...):
        ...
    

