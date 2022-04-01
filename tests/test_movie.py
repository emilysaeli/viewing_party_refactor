import pytest
from viewing_party.movie import Movie

def test_1():
    # Arrange
    title = "Up"
    genre = "Dog doesn't die"
    rating = 10
    host = "Disney+"
    # Act
    up_movie = Movie(title = title, genre = genre, rating = rating, host = host)
    # Assert
    assert up_movie.title == title
    assert up_movie.genre == genre
    assert up_movie.rating == rating
    assert up_movie.host == host