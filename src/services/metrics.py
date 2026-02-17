from __future__ import annotations

from typing import Final
from prometheus_client import Counter, Gauge, Histogram, start_http_server

# Order lifecycle metrics
orders_placed_counter: Final = Counter(
    "pm_mm_orders_placed_total", "Total orders placed", ["side", "outcome"]
)
orders_filled_counter: Final = Counter(
    "pm_mm_orders_filled_total", "Total orders filled", ["side", "outcome"]
)
orders_cancelled_counter: Final = Counter(
    "pm_mm_orders_cancelled_total", "Total orders cancelled"
)

# Position and risk metrics
inventory_gauge: Final = Gauge(
    "pm_mm_inventory", "Current inventory positions", ["type"]
)
exposure_gauge: Final = Gauge("pm_mm_exposure_usd", "Current net exposure in USD")

# Market quality metrics
spread_gauge: Final = Gauge("pm