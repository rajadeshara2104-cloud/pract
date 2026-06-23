class Taxi:
    def __init__(self, taxi_id, driver_name):
        self.taxi_id = taxi_id
        self.driver_name = driver_name
        self.available = True

    def book(self):
        self.available = False

    def release(self):
        self.available = True


class Booking:
    def __init__(self, customer_name, pickup, destination, distance):
        self.customer_name = customer_name
        self.pickup = pickup
        self.destination = destination
        self.distance = distance

    def calculate_fare(self):
        base_fare = 50
        per_km = 15
        return base_fare + (self.distance * per_km)


class TaxiBookingSystem:
    def __init__(self):
        self.taxis = []

    def add_taxi(self, taxi):
        self.taxis.append(taxi)

    def show_available_taxis(self):
        print("\nAvailable Taxis:")
        found = False

        for taxi in self.taxis:
            if taxi.available:
                print(f"Taxi ID: {taxi.taxi_id}")
                print(f"Driver : {taxi.driver_name}")
                print("-------------------")
                found = True

        if not found:
            print("No taxis available.")

    def book_taxi(self):
        self.show_available_taxis()

        taxi_id = int(input("Enter Taxi ID: "))

        for taxi in self.taxis:
            if taxi.taxi_id == taxi_id and taxi.available:

                customer = input("Enter Customer Name: ")
                pickup = input("Enter Pickup Location: ")
                destination = input("Enter Destination: ")
                distance = float(input("Enter Distance (KM): "))

                booking = Booking(
                    customer,
                    pickup,
                    destination,
                    distance
                )

                fare = booking.calculate_fare()

                taxi.book()

                print("\n===== BOOKING RECEIPT =====")
                print("Customer :", customer)
                print("Taxi ID  :", taxi.taxi_id)
                print("Driver   :", taxi.driver_name)
                print("Pickup   :", pickup)
                print("Drop     :", destination)
                print("Distance :", distance, "KM")
                print("Fare     : ₹", fare)
                print("===========================")
                return

        print("Taxi not available!")

    def release_taxi(self):
        taxi_id = int(input("Enter Taxi ID to Release: "))

        for taxi in self.taxis:
            if taxi.taxi_id == taxi_id:
                taxi.release()
                print("Taxi Released Successfully!")
                return

        print("Taxi Not Found!")


# Main Program
system = TaxiBookingSystem()

system.add_taxi(Taxi(101, "Rajesh"))
system.add_taxi(Taxi(102, "Suresh"))
system.add_taxi(Taxi(103, "Mahesh"))

while True:
    print("\n===== TAXI BOOKING SYSTEM =====")
    print("1. Show Available Taxis")
    print("2. Book Taxi")
    print("3. Release Taxi")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        system.show_available_taxis()

    elif choice == 2:
        system.book_taxi()

    elif choice == 3:
        system.release_taxi()

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")