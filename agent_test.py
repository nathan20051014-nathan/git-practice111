"""Helpers for displaying robot status."""


def show_robot_status(
    robot_name: str = "Test Robot",
    speed: float = 0,
    is_running: bool = False,
) -> None:
    """Print the robot name, speed, and current running status."""
    status = "running" if is_running else "stopped"
    print(f"Robot name: {robot_name}")
    print(f"Speed: {speed}")
    print(f"Running status: {status}")
