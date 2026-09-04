"""Temperature sensor reading helpers."""

from __future__ import annotations

from collections.abc import Callable
from math import isfinite


def read_temperature(reader: Callable[[], float]) -> float | None:
    """Read a Celsius temperature from a temperature sensor driver.

    Returns ``None`` after reporting a driver failure or an invalid reading.
    """
    try:
        temperature_celsius = float(reader())
    except (OSError, TypeError, ValueError) as error:
        print(f"Temperature sensor read error: {error}")
        return None

    if not isfinite(temperature_celsius):
        print("Temperature sensor read error: value must be a finite number")
        return None

    return temperature_celsius
