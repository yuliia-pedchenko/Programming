from datetime import date

class Movies:
    def __init__(self, movie_id, title, duration, genre, release_date):
        self.__movie_id = movie_id
        self.title = title
        self.duration = duration
        self.genre = genre
        self.release_date = release_date

    def get_movie_id(self):
        return self.__movie_id

    def set_movie_id(self, movie_id):
        self.__movie_id = movie_id

    def is_released(self):
        today = date.today()
        if today <= self.release_date:
            print(f"The movie {self.title} has been released.")
        else:
            print(f"The movie {self.title} hasn't been released yet.")

    @staticmethod
    def convert_minutes_to_hours(minutes):
        hours = minutes // 60
        remaining_minutes = minutes % 60
        if remaining_minutes < 10:
            return f"{hours}:0{remaining_minutes}"
        else:
            return f"{hours}:{remaining_minutes}"


class Ratings:
    def __init__(self, rating):
        self.rating = rating

    def get_rating(self):
        return f"Rating: {self.rating}/5.0"

class RatedMovies(Movies, Ratings):
    def __init__(self, movie_id, title, duration, genre, rating, release_date):
        Movies.__init__(self, movie_id, title, duration, genre, release_date)
        Ratings.__init__(self, rating)

    def update_rating(self, rating):
        if 0.0 <= rating <= 5.0:
            self.rating = rating
        else:
            raise ValueError("Rating must be between 0.0 and 5.0")

    def movie_info(self):
        print(f"movie_id: {self.get_movie_id()}\n"
              f"title: {self.title}\n"
              f"duration: {self.convert_minutes_to_hours(self.duration)}\n"
              f"genre: {self.genre}\n"
              f"rating: {self.rating}\n"
              f"release_date: {self.release_date}\n")

class UnratedMovies(Movies, Ratings):
    def __init__(self, movie_id, title, duration, genre, release_date):
        Movies.__init__(self, movie_id, title, duration, genre, release_date)
        Ratings.__init__(self, rating=-1)

    def movie_info(self):
        print(f"movie_id: {self.get_movie_id()}\n"
              f"title: {self.title}\n"
              f"duration: {self.convert_minutes_to_hours(self.duration)}\n"
              f"genre: {self.genre}\n"
              f"rating: There is no rating yet.\n"
              f"release_date: {self.release_date}\n")

movie_1 = RatedMovies(1, "Three-body problem", 120, "Sci-fi", 4.6, date(2024,9, 23))
movie_2 = RatedMovies(2, "The Green Mile", 189, "Drama", 4.9, date(2024,11, 2))
movie_3 = UnratedMovies(3, "I forgot other existing movies", 146, "Documentary", date(2023,7, 11))
movie_4 = UnratedMovies(4, "I still don't remember", 93, "Comedy", date(2025,4, 20))

movie_1.movie_info()
movie_3.movie_info()
movie_3.set_movie_id(5)
print(movie_3.get_movie_id())
movie_4.is_released()
movie_3.is_released()

