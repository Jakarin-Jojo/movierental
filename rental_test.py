import unittest
from rental import *
from movie import *


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.catalog = MovieCatalog()
        self.new_movie = self.catalog.get_movie("Eternals")
        self.regular_movie = self.catalog.get_movie("A Tenant")
        self.childrens_movie = self.catalog.get_movie("Weathering With You")

        self.price_code_new_release = PriceCode.for_movie(self.new_movie)
        self.price_code_regular = PriceCode.for_movie(self.regular_movie)
        self.price_code_childrens = PriceCode.for_movie(self.childrens_movie)

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        self.assertEqual("Weathering With You", self.childrens_movie.get_title())
        self.assertEqual(PriceCode.childrens, self.price_code_childrens)

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1, self.price_code_new_release)
        self.assertEqual(rental.get_charge(), 3.0)
        rental = Rental(self.new_movie, 5, self.price_code_new_release)
        self.assertEqual(rental.get_charge(), 15.0)
        rental = Rental(self.regular_movie, 10, self.price_code_regular)
        self.assertEqual(rental.get_charge(), 14.0)
        rental = Rental(self.childrens_movie, 5, self.price_code_childrens)
        self.assertEqual(rental.get_charge(), 4.5)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 5, self.price_code_new_release)
        self.assertEqual(rental.get_frequent_rental_points(), 5)
        rental = Rental(self.regular_movie, 10, self.price_code_regular)
        self.assertEqual(rental.get_frequent_rental_points(), 1)
        rental = Rental(self.childrens_movie, 20, self.price_code_childrens)
        self.assertEqual(rental.get_frequent_rental_points(), 1)


if __name__ == '__main__':
    unittest.main()
