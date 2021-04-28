import unittest
from bikeRental import BikeRental
from customer import Customer
from datetime import datetime, timedelta

class BikeRentalTest(unittest.TestCase):

    def test_bike_rental_display_correct_stock(self):
        shop1 = BikeRental()
        shop2 = BikeRental(10)
        self.assertEqual(shop1.displayStock(), 0)
        self.assertEqual(shop2.displayStock(),10)

    def test_rentBikeOnHourlyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikesOnHourlyBasis(-1), None)


class CustomerTest(unittest.TestCase):

    def test_returnBike(self):
        customer = Customer()
        customer.rentalBasics = 1
        customer.bikes = 2
        customer.rentalTime = datetime.now()

        self.assertEqual(customer.returnBike(),(2,1,datetime.now()))

    def test_returnBike_withInvalidInput(self):
        customer = Customer()
        customer.rentalBasics = 1
        customer.bikes = 0
        customer.rentalTime = 0

        self.assertEqual(customer.returnBike(),(0,0,0))