🚌 Bus Ticket Booking Script
This is a simple Python script for booking bus tickets. It lets you choose a route, book seats, and see the total price.

It checks if seats are available and calculates your fare, which includes an extra fee (surcharge) based on the travel distance.

✨ What It Does
Shows Routes: Has a pre-set list of bus routes (like Pune to Nashik).

Checks Seats: Makes sure there are enough empty seats for your booking.

Calculates Price:

Starts with a base fare for the route.

Adds an extra fee (surcharge) based on the distance (longer trips have a higher fee).

Calculates the total cost for all passengers.

Updates Seat Count: After you book, it shows how many seats are left.

Shows Errors: Tells you if the route isn't found or if there aren't enough seats.

🚀 How to Use It
Make sure you have Python installed on your computer.

Save the code as a Python file (like mini_project2.py).

Open your terminal or command prompt.

Go to the folder where you saved the file.

Run the script by typing:

Bash

python "mini project2.py"
Answer the two questions it asks:

Select the journey: (Type B1, B2, B3, or B4)

Enter number of passengers: (Type a number, like 2)

Example:

Select the journey: B2
Enter number of passengers: 3
Fare/person=300 | Total=900 | Seats left=32
⚙️ How It Works (Step-by-Step)
Stored Data: The script stores all bus routes in a dictionary called Routes. This includes the start, end, distance, seats, and base price for each route.

User Input: It asks you for the Route ID (e.g., B1) and the number of passengers.

Checks:

First, it checks if the Route ID you entered is valid.

If it is, it then checks if there are enough seats for the number of passengers you want.

Price Calculation:

If there are enough seats, it calculates an extra fee (surcharge) based on the route's distance.

The total price per person is the base_fare + surcharge.

The total bill is price_per_person * number_of_passengers.

Final Message: It prints a message showing the price per person, the total bill, and how many seats are left.

💡 Ideas for Later
This is a great start! Here are ways you could make it better:

Save Seat Counts: Store the number of seats in a file, so the count doesn't reset every time you run the script.

Add a Menu: Let the user choose to "Book a Ticket," "See All Routes," or "Quit."

Cancel Bookings: Add a feature to cancel a booking and add the seats back.
