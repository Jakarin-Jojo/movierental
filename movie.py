from typing import List


class Movie:
    """A movie available for rent."""

    def __init__(self, title: str, year: int, genre: List[str]):
        # Initialize a new movie.
        self._genre = genre
        self._year = year
        self._title = title

    def get_title(self) -> str:
        return self._title

    def get_year(self):
        return self._year

    def get_genre(self):
        return self._genre

    def is_genre(self, string):
        """Returns: true if the string parameter matches one of the movie’s genre."""
        if string in self._genre:
            return True
        return False

    def __str__(self) -> str:
        return self.title
