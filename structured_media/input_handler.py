from models.movie import Movie
from models.tv_series import TVSeries

def media_input() -> Movie | TVSeries:
    """Function to get user
    input for a media item and
    return either a Movie or TVSeries
    instance based on the input.
    """
    media_type = input('Enter media type (movie/tv): ').strip().lower()

    if media_type not in ['movie', 'tv']:
        """If the user enters an invalid media type, raise a ValueError with a clear message."""
        raise ValueError('Invalid media type. Please enter "movie" or "tv".')

    title = input('Enter title: ').strip()
    year = int(input('Enter year: ').strip())
    director = input('Enter director: ').strip()
    duration = int(input('Enter duration (in minutes): ').strip())

    if media_type == 'movie':
        return Movie(title, year, director, duration)

    seasons = int(input('Enter number of seasons: ').strip())
    total_episodes = int(input('Enter total episodes: ').strip())
    return TVSeries(title, year, director, duration, seasons, total_episodes)