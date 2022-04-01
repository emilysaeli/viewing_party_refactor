class Person:
    def __init__(self, name, watched, subscriptions):
        self.name = name
        self.watched = watched
        self.friends = []
        self.subscriptions = subscriptions

    def add_watched(self, movie):
        self.watched.append(movie)
        return self.watched

    def get_num_watched(self):
        return len(self.watched)