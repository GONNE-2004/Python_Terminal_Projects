from models.movie import Movie


class TVSeries(Movie):
    """Child class representing a TV series, which is a type of movie with additional attributes for seasons and total episodes."""

    def __init__(self, title, year, director, duration, seasons, total_episodes) -> None:
        # Call the parent constructor to initialize common attributes
        super().__init__(title, year, director, duration)

        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')

        self.seasons = seasons
        self.total_episodes = total_episodes

    def __str__(self) -> str:
        return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'