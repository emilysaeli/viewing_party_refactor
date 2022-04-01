import pytest
from viewing_party.person import Person

def test_initialize_Person():
    # Arrange
    name = "Ann"
    watched = []
    subscriptions = []

    # Act
    person = Person(name = name, watched = watched, subscriptions = subscriptions)
    # Assert
    assert person.name == name
    assert person.watched == watched
    assert person.subscriptions == subscriptions

def test_add_movie_to_watched():
    auberon = Person(name = "Auberon", watched=[], subscriptions=[])
    new_movie = "Shrek" 

    movie_watched = auberon.add_watched(new_movie)

    assert new_movie in movie_watched == ["Shrek"]

# def test_driver_add_trip():
#     batman = Driver()
#     original_trip_length = len(batman.trips)
#     valid_trip = Trip()

#     result = batman.add_trip(valid_trip)

#     assert result
#     assert len(batman.trips) is original_trip_length + 1
#     assert valid_trip in batman.trips