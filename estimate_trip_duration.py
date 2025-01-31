def estimate_trip_duration(distance, average_speed):


    # Check if distance is positive, if not ask the user to correct it
    while distance <= 0:
        print("Distance must be a positive value.")
        distance = float(input("Please enter a valid distance (in kilometers): "))


    # Check if speed is positive, if not ask the user to correct it
    while average_speed < 0:
        print("Speed must be a positive value.")
        average_speed = float(input("Please enter a valid speed (in kilometers per hour): "))


    # Calculate the estimated time
    estimated_time = distance / average_speed
    print(f"The estimated trip duration is {estimated_time:.2f} hour.")


# Example usage
distance = float(input("Please enter a distance (in kilometers): "))
average_speed = float(input("Please enter an averagespeed (in kilometers per hour): "))




estimate_trip_duration(distance, average_speed)
