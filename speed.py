# Author: Dan Richmond-Martina

def calculate_speed(distance, time):
    """
    Takes the distance and time and computes the value of speed
    :param distance: An integer value of the distance to be travelled in kilometers
    :param time: An integer value of the desired time in hours
    :return: The value of speed
    """
    speed = distance // time
    return speed


def display_speed():
    print("\n3: Calculate Speed\n")
    distance = int(input("Enter the desired distance in KM: "))
    time = int(input("Enter the desired time in hours: "))
    speed = calculate_speed(distance, time)
    print("To travel " + str(distance), "KM in " + str(time), "hours you need to travel at " + str(speed), "KM an hour.")
