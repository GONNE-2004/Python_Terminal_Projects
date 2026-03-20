from models.movie import Movie
from models.tv_series import TVSeries
from errors import MediaError

class MediaCatalogue:
    """A catalogue to store movies and TV series."""

    def __init__(self) -> None:
        self.items = []

    def add(self, media_item) -> None:
        """Add a media item to the catalogue, ensuring it is either a Movie or TVSeries instance."""
        if not isinstance(media_item, (Movie, TVSeries)):
            raise MediaError(
                'Only Movie and TVSeries instances can be added to the catalogue', media_item)
        self.items.append(media_item)

    def get_movies(self) -> list[Movie]:
        return [item for item in self.items if type(item) is Movie]

    def get_tv_series(self) -> list[TVSeries]:
        return [item for item in self.items if type(item) is TVSeries]

    def __str__(self) -> str:
        if not self.items:
            return 'Media Catalogue (empty)'

        movies = self.get_movies()
        series = self.get_tv_series()

        result = f'Media Catalogue ({len(self.items)} items):\n\n'

        if movies:
            result += '=== MOVIES ===\n'
            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'

        if series:
            result += '\n=== TV SERIES ===\n'
            for i, s in enumerate(series, 1):
                result += f'{i}. {s}\n'
        return result