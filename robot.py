robot_name = "Carbon Walker"
speed = 10


def start_robot():
    print(f"{robot_name} started")
    print(f"Current speed: {speed}")


def read_temperature():
    temperature = -13.9
    print(f"Temperature: {temperature} C")


start_robot()
read_temperature()