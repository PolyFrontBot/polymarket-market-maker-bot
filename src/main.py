from __future__ import annotations

import asyncio
import signal
import time
from typing import Any

import structlog
from dotenv import load_dotenv

from src.config import Settings, get_settings
from src.execution.order_executor import OrderExecutor
from src.inventory.inventory_manager import InventoryManager
from src.logging_config import configure_logging
from src.market_maker.quote_engine import QuoteEngine
from src.polymarket.order_signer import OrderSigner
from src.polymarket.rest_client import PolymarketRestClient
from src.polymarket.websocket_client import PolymarketWebSocketClient
from src.risk.risk_manager import RiskManager
from src.services import AutoRedeem, start_metrics_server

logger = structlog.get_logger(__name__)


class MarketMakerBot:
    """
    Main orchestrator for the Polymarket market making bot.
    
    Coordinates WebSocket feeds, inventory tracking,