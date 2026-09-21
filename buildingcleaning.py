# First ask how many buildings need to be cleaned
buildings = input("How many buildings need to be cleaned: ")
buildings = int(buildings)

# Ask travel time between buildings
travel_time = input("How many minutes to travel between buildings: ")
travel_time = int(travel_time)

# This is the amount of time it takes to clean one building
cleaning_time = input("How many minutes to clean one building: ")
cleaning_time = int(cleaning_time)

total_time = (buildings * cleaning_time) + ((buildings - 1) * travel_time)
print(f"Total time needed: {total_time} minutes")
