class Flight:
    def __init__(self, flight_number, origin, destination, seats):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.seats = seats
        self.passengers = []

    def book_ticket(self, passenger):
        if len(self.passengers) < self.seats:
            self.passengers.append(passenger)
            print(f"Ticket booked for {passenger}.")
        else:
            print("Sorry, flight is full.")

    def cancel_ticket(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"Ticket for {passenger} canceled.")
        else:
            print(f"No booking found for {passenger}.")

    def view_passenger_list(self):
        if self.passengers:
            print(f"Passenger list for Flight {self.flight_number}:")
            for p in self.passengers:
                print(f"- {p}")
        else:
            print("No passengers on this flight yet.")


class AirlineManagementSystem:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight_number, origin, destination, seats):
        if flight_number not in self.flights:
            flight = Flight(flight_number, origin, destination, seats)
            self.flights[flight_number] = flight
            print(f"Flight {flight_number} added successfully.")
        else:
            print("Flight number already exists.")

    def book_ticket(self, flight_number, passenger):
        if flight_number in self.flights:
            self.flights[flight_number].book_ticket(passenger)
        else:
            print("Flight not found.")

    def cancel_ticket(self, flight_number, passenger):
        if flight_number in self.flights:
            self.flights[flight_number].cancel_ticket(passenger)
        else:
            print("Flight not found.")

    def view_flights(self):
        if self.flights:
            print("Available flights:")
            for flight in self.flights.values():
                print(f"Flight {flight.flight_number}: {flight.origin} -> {flight.destination}")
        else:
            print("No flights available.")

    def view_passengers(self, flight_number):
        if flight_number in self.flights:
            self.flights[flight_number].view_passenger_list()
        else:
            print("Flight not found.")


def main():
    system = AirlineManagementSystem()

    while True:
        print("\n--- Airline Management System ---")
        print("1. Add Flight")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. View Flights")
        print("5. View Passengers")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            flight_number = input("Enter flight number: ")
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            seats = int(input("Enter number of seats: "))
            system.add_flight(flight_number, origin, destination, seats)

        elif choice == '2':
            flight_number = input("Enter flight number: ")
            passenger = input("Enter passenger name: ")
            system.book_ticket(flight_number, passenger)

        elif choice == '3':
            flight_number = input("Enter flight number: ")
            passenger = input("Enter passenger name: ")
            system.cancel_ticket(flight_number, passenger)

        elif choice == '4':
            system.view_flights()

        elif choice == '5':
            flight_number = input("Enter flight number: ")
            system.view_passengers(flight_number)

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
