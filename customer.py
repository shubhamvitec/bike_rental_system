class Customer:

    def __init__(self):
        self.bikes = 0
        self.rentalBasics = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
        bikes = input("How many bikes you want to rent? ")

        try:
            bikes = int(bikes)
        except ValueError:
            print("Thats not a positive integer !")
            return -1

        if bikes < 1:
            return -1
        else:
            self.bikes = bikes
            return self.bikes

    def returnBike(self):
        if self.bikes and self.rentalBasics and self.rentalTime:
            return self.bikes, self.rentalBasics, self.rentalTime
        else:
            return 0,0,0