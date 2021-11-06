from typing import List
import pandas as pd


class Movie:
    """A movie available for rent."""

    def __init__(self, title: str, year: int, genre: List[str]):
        # Initialize a new movie.
        self._genre = genre
        self._year = year
        self._title = title

    def get_title(self) -> str:
        return self._title

    def get_year(self) -> int:
        return self._year

    def get_genre(self) -> List[str]:
        return self._genre

    def is_genre(self, string) -> bool:
        """Returns: true if the string parameter matches one of the movie’s genre."""
        if string in self._genre:
            return True
        return False

    def __str__(self) -> str:
        return self._title


class MovieCatalog:
    """A movie catalog for renting movies."""

    def __init__(self):
        self.movie_list = pd.read_csv("movies.csv")

    def get_movie(self, title: str) -> Movie:
        """Get a movie from a movie.csv"""
        movie = self.movie_list[self.movie_list['title'] == title]
        movie_title = movie.iloc[0]['title']
        year = int(movie.iloc[0]['year'])
        genre = movie.iloc[0]['genres'].split('|')
        return Movie(title=movie_title, year=year, genre=genre)
