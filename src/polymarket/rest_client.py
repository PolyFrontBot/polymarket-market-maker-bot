from __future__ import annotations

from typing import Any

import httpx
import structlog

from src.config import Settings

logger = structlog.get_logger(__name__)


class PolymarketRestClient:
    """Async client for interacting with the Polymarket REST API."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.base_url = settings.polymarket_api_url
        # TODO: Make timeout configurable via Settings
        self.client = httpx.AsyncClient(timeout=30.0)

    async def get_markets(self, active: bool = True, closed: bool = False) -> list[dict[str, Any]]:
        try:
            params = {"active": str(active).lower(), "closed": str(closed).lower()}
            response = await self.client.get(f"{self.base_url}/markets", params=params