class MediaError(Exception):
    """Custom exception for media-related errors."""

    def __init__(self, message, obj) -> None:
        """Initialize the MediaError with a message and the object that caused the error."""
        super().__init__(message)
        self.obj = obj