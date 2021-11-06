from typing import List


class Movie:
    """A movie available for rent."""

    def __init__(self, title: str, year: int, genre: List[str]):
        # Initialize a new movie.
        self.genre = genre
        self.year = year
        self.title = title

    def get_title(self) -> str:
        return self.title

    def get_year(self):
        return self.year

    def get_genre(self):
        return self.genre

    def __str__(self) -> str:
        return self.title
