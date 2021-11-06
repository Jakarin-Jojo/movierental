from enum import Enum
from movie import *
from datetime import datetime
import logging


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    regular = {"price": lambda days: 2 if days <= 2 else 2 + 1.5 * (days - 2),
               "frp": lambda days: 1
               }
    childrens = {"price": lambda days: 1.5 if days <= 3 else 1.5 + 1.5 * (days - 3),
                 "frp": lambda days: 1
                 }

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def point(self, day: int) -> float:
        pointing = self.value["frp"]
        return pointing(day)

    @staticmethod
    def for_movie(movie: Movie):
        year = datetime.now().year
        if movie.get_year() == year:
            return PriceCode.new_release
        elif 'Children' in movie.get_genre():
            return PriceCode.childrens
        return PriceCode.regular


class Rental:
    """
	A rental of a movie by customer.
    From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	But for simplicity of the example only a days_rented field is used.
	"""

    def __init__(self, movie: Movie, days_rented: int, price_code: PriceCode):
        """Initialize a new movie rental object for a movie with known rental period (daysRented)."""
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code

    def get_movie(self) -> Movie:
        return self.movie

    def get_title(self) -> str:
        return self.movie.get_title()

    def get_days_rented(self) -> int:
        return self.days_rented

    def get_charge(self) -> float:
        return self.price_code.price(self.days_rented)

    def get_frequent_rental_points(self) -> float:
        return self.price_code.point(self.days_rented)
