from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    environment: str = "development"
    log_level: str = "INFO"

    # Polymarket API
    polymarket_api_url: str = Field(
        default="https://clob.polymarket.com", description="Polymarket CLOB API base URL"
    )
    polymarket_ws_url: str = Field(
        default="wss://clob-ws.polymarket.com", description="Polymarket WebSocket URL"
    )
    
    # Authentication
    private_key: str = Field(description="Ethereum private key for signing orders")