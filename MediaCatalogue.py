# """System model in (plain English)
# Entities
# A Movie is a valid media item
# A TVSeries is also a Movie, but with extra fields
# A MediaCatalogue owns a list of media items
# Rules
# Only Movie/TVSeries objects may be added
# Movies and TV series must be separated when displaying
# Empty catalogue prints a special message
# Errors should be clear and meaningful

# Pseudocode:
# IF catalogue is empty
#     RETURN "Media Catalogue (empty)"
# GET all movies
# GET all tv series
# START result string with header and item count
# IF movies exist
#     ADD movies section header
#     FOR each movie
#         ADD numbered movie line
# IF tv series exist
#     ADD tv series section header
#     FOR each series
#         ADD numbered series line
# RETURN result
# """
class MediaError(Exception):
    """Custom exception for media-related errors."""

    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj


class Movie:
    """Parent class representing a movie with title, year, director, and duration."""

    def __init__(self, title, year, director, duration) -> None:
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        if not director.strip():
            raise ValueError('Director cannot be empty')
        if duration <= 0:
            raise ValueError('Duration must be positive')
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    def __str__(self) -> str:
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'


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


class MediaCatalogue:
    """A catalogue to store movies and TV series."""

    def __init__(self) -> None:
        self.items = []

    def add(self, media_item) -> None:
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


# Create an instance of the MediaCatalogue to store our media items
catalogue = MediaCatalogue()


def media_input() -> Movie | TVSeries:
    media_type = input('Enter media type (movie/tv): ').strip().lower()
    title = input('Enter title: ').strip()
    year = int(input('Enter year: ').strip())
    director = input('Enter director: ').strip()
    duration = int(input('Enter duration (in minutes): ').strip())

    if media_type == 'movie':
        return Movie(title, year, director, duration)

    elif media_type == 'tv':
        seasons = int(input('Enter number of seasons: ').strip())
        total_episodes = int(input('Enter total episodes: ').strip())
        return TVSeries(title, year, director, duration, seasons, total_episodes)

    else:
        raise ValueError('Invalid media type. Please enter "movie" or "tv".')


running = True
while running:
    try:
        command = input('Enter command (add/exit): ').strip().lower()
        if command == 'exit':
            running = False
            print('Exiting the media catalogue. Goodbye!')
            break

        if command != 'add':
            print('Invalid command. Please enter "add" or "exit".')
            continue

        media_item = media_input()
        # add the media item to the catalogue after getting the input
        catalogue.add(media_item)
        print(catalogue)

    except ValueError as e:
        print(f'Validation Error: {e}')

    except MediaError as e:
        # This will print the error message along with the object that caused the error
        print(f'Media Error: {e} - Object: {e.obj}')
