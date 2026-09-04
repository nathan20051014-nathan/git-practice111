"""Temperature acquisition and over-temperature alarm helpers."""

from __future__ import annotations

from collections.abc import Callable
from math import isfinite

DEFAULT_TEMPERATURE_LIMIT = 80.0


def read_temperature(reader: Callable[[], float]) -> float:
    """Read one temperature value from a sensor driver in degrees Celsius.

    The driver is injected so this module remains independent of a particular
    hardware sensor implementation.
    """
    temperature = float(reader())
    if not isfinite(temperature):
        raise ValueError("temperature must be a finite number")
    return temperature


def is_over_temperature(
    temperature: float, limit: float = DEFAULT_TEMPERATURE_LIMIT
) -> bool:
    """Return whether *temperature* is strictly above the configured limit."""
    if not isfinite(temperature) or not isfinite(limit):
        raise ValueError("temperature and limit must be finite numbers")
    return temperature > limit


def trigger_over_temperature_alarm(temperature: float, limit: float) -> None:
    """Issue the default over-temperature alarm."""
    print(f"ALARM: temperature {temperature:.1f} C exceeds limit {limit:.1f} C")


def monitor_temperature(
    reader: Callable[[], float],
    limit: float = DEFAULT_TEMPERATURE_LIMIT,
    alarm: Callable[[float, float], None] = trigger_over_temperature_alarm,
) -> tuple[float, bool]:
    """Read the sensor and trigger *alarm* when its temperature exceeds *limit*."""
    temperature = read_temperature(reader)
    over_temperature = is_over_temperature(temperature, limit)
    if over_temperature:
        alarm(temperature, limit)
    return temperature, over_temperature
