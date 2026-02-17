from __future__ import annotations

import asyncio
import json
from typing import Any, Callable, Awaitable

import structlog
import websockets

from src.config import Settings

logger = structlog.get_logger(__name__)


class PolymarketWebSocketClient:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.ws_url = settings.polymarket_ws_url
        self.websocket: websockets.WebSocketServerProtocol | None = None
        # Maps specific message event types (e.g., 'book') to their corresponding async callbacks.
        self.message_handlers: dict[str, Callable[[dict[str, Any]], Awaitable[None]]] = {}
        self.running = False

    def register_handler(self, message_type: str, handler: Callable[[dict[str, Any]], Awaitable[None]]) -> None:
        """Registers an async callback