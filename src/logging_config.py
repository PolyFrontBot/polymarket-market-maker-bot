from __future__ import annotations

import logging
import sys
from typing import Literal

import structlog


def configure_logging(level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO") -> None:
    """Configures the root logger and structlog to output JSON formatted logs.

    This setup integrates structlog with the standard library logging module,
    ensuring that all logs are output in a consistent JSON format suitable
    for production environments and log aggregation services.
    """
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=level,
    )

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.process