# Shivam Mugaji Jahane
# Enrolement Number-2502140075

# Bus Ticket Project
# Routes: 'ID': [Start, Dest, KM, Seats, Fare]
Routes = {
    'B1': ['Pune', 'Nashik', 210, 40, 250],
    'B2': ['Mumbai', 'Pune', 150, 35, 200],
    'B3': ['Delhi', 'Jaipur', 280, 45, 400],
    'B4': ['Bangalore', 'Chennai', 350, 40, 500]}
# Booking Input
Journey = input("Select the journey: ")  # Input which journey to book
passengers_to_book = int(input("Enter number of passengers: "))

if Journey in Routes:
    route_info = Routes[Journey]
    distance = route_info[2]
    available_seats = route_info[3]
    fare = route_info[4]

    if passengers_to_book <= available_seats:

        # Calculate fare
        # surcharge is an extra fee you add based on the distance.
        surcharge = 0
        if distance <= 100:
            surcharge = 50
        elif distance <= 300:
            surcharge = 100
        else:
            surcharge = 150
        fare_per_person = fare + surcharge
        total_fare = fare_per_person * passengers_to_book

        # Update seats
        new_seat_count = available_seats - passengers_to_book
        Routes[Journey][3] = new_seat_count

        # Print output
        print(f"Fare/person={fare_per_person} | Total={total_fare} | Seats left={new_seat_count}")

    else:
        print(f"Booking failed. Only {available_seats} seats left.")

else:
    print(f"Error: Route {Journey} not found.")








