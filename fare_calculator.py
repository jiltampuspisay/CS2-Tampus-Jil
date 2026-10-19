# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ").strip()

if name == "":
    print("Error: Name is required.")
    name = input("Please enter your name: ")

distance = float(input("Enter distance (km): "))

if distance <= 0:
    print("Error: Distance must be greater than 0.")
    distance = float(input("Please enter distance greater than 0: "))

passengers = int(input("Enter number of passengers: "))

if passengers <= 0:
    print("Error: Passengers must be more than 0.")
    passengers = int(input("Please enter number of passengers more than 0: "))

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
