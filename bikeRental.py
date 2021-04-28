import datetime

class BikeRental:

    def __init__(self, stock=0):
        self.stock = stock

    def displayStock(self):
        print("Currently we have {} bikes in stock.".format(self.stock))
        return self.stock

    def rentBikesOnHourlyBasis(self, n):
        if n <= 0 :
            print("Number of bikes should be positive")
        elif n > self.stock:
            print("Sorry we don't have {} bike in stock currently".format(n))
            print("Currently available no. of bikes are : {}".format(self.stock))
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on hourly basis today at {}".format(n, now))
            print("you will be charged $5 per hour per bike")
            print("We hope that you enjoyed our service")

            self.stock = self.stock-n
            return now

    def rentBikesOnDailyBasis(self, n):
        if n <= 0 :
            print("Number of bikes should be positive")
        elif n > self.stock:
            print("Sorry we don't have {} bike in stock currently".format(n))
            print("Currently available no. of bikes are : {}".format(self.stock))
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on daily basis today at {}".format(n, now))
            print("you will be charged $20 per hour per bike")
            print("We hope that you enjoyed our service")

            self.stock = self.stock-n
            return now

    def rentBikesOnWeeklyBasis(self, n):
        if n <= 0 :
            print("Number of bikes should be positive")
        elif n > self.stock:
            print("Sorry we don't have {} bike in stock currently".format(n))
            print("Currently available no. of bikes are : {}".format(self.stock))
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {}".format(n, now))
            print("you will be charged $60 per hour per bike")
            print("We hope that you enjoyed our service")

            self.stock = self.stock-n
            return now


    def returnBikes(self, request):
        n, rentalBasics, rentalTime = request
        bill = 0

        if rentalTime and rentalBasics and n:
            self.stock +=n
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            print("*****now : {}".format(now))
            print("*****rentalTime :  {}".format(rentalTime))
            print("*****rentalPeriod :  {}".format(rentalPeriod))


            if rentalBasics == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * n

            if rentalBasics == 2:
                bill = round(rentalPeriod.seconds / 3600) * 20 * n

            if rentalBasics == 3:
                bill = round(rentalPeriod.seconds / 3600) * 60 * n

            if (3 <= n <= 5):
                print("yout are elligible for family discount of 30%")
                bill = bill * 0.7
            
            print("Total Bill: {}".format(bill))
            return bill

        else:
            return None