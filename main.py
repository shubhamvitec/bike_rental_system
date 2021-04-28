from bikeRental import BikeRental
from customer import Customer

def main():
    shop = BikeRental(100)
    customer = Customer()

    while True:

        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $20
        4. Request a bike on weekly basis $60
        5. Return a bike
        6. Exit
        """)

        choice = input("Enter your choice ? ")
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an integer value you entered !")
            continue

        if choice == 1:
            shop.displayStock()

        elif choice == 2:
            customer.rentalTime = shop.rentBikesOnHourlyBasis(customer.requestBike())
            customer.rentalBasics = 1

        elif choice == 3:
            customer.rentalBasics = 2
            customer.rentalTime = shop.rentBikesOnDailyBasis(customer.requestBike())
        
        elif choice == 4:
            customer.rentalBasics = 3
            customer.rentalTime = shop.rentBikesOnWeeklyBasis(customer.requestBike())

        elif choice == 5:
            customer.bill = shop.returnBikes(customer.returnBike())
            customer.rentalBasics, customer.rentalTime, customer.bikes = 0,0,0

        elif choice == 6:
            break
        else:
            print("INVALID Choice")

if __name__=="__main__":
    main()