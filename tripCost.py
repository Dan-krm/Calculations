# Author: Dan Richmond-Martina

def trip_cost(air_fare, room_cost, number_of_people, number_of_nights):
    """
    Computes the total amount due for a trip
    :param air_fare: A float which is the cost of the flight in dollars
    :param room_cost: A float which is the cost of the room in dollars
    :param number_of_people: An integer for the number of people attending the trip
    :param number_of_nights: An integer for the number of nights stayed at the hotel
    :return: The total cost of the trip per person
    """
    number_of_rooms = number_of_people // 2 + number_of_people % 2
    total = ((number_of_rooms * room_cost * number_of_nights) + (number_of_people * air_fare))
    return total


def display_trip_cost():
    print("\n4: Calculate a Trips Cost\n")
    # Call the trip_cost function using user inputs for each parameter, then display the results
    group_total = trip_cost(air_fare=float(input("Enter the the cost of the flight: ")),
                            room_cost=float(input("Enter the cost of a room per night: ")),
                            number_of_people=int(input("Enter the number of people: ")),
                            number_of_nights=int(input("Enter the number of nights: ")))
    print("The total cost of the trip for the group is: $" + str(group_total))
