"""Motor control functions for the robot."""

import math

_is_running = False
_speed = 0


def start_motor():
    """Start the motor."""
    global _is_running
    _is_running = True
    print("Motor started")


def stop_motor():
    """Stop the motor and reset its speed."""
    global _is_running, _speed
    _is_running = False
    _speed = 0
    print("Motor stopped")


def set_motor_speed(speed):
    """Set the motor speed to a non-negative numeric value."""
    if (
        isinstance(speed, bool)
        or not isinstance(speed, (int, float))
        or not math.isfinite(speed)
    ):
        raise TypeError("Motor speed must be a number")
    if speed < 0:
        raise ValueError("Motor speed cannot be negative")

    global _speed
    _speed = speed
    print(f"Motor speed set to {_speed}")


def set_speed(speed):
    """Set the motor speed."""
    set_motor_speed(speed)
