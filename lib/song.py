class Song:
    """
    Represents a song with name, artist, and genre.
    Tracks class-level statistics about all songs created.
    """

    # Class attributes to track all songs
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        """
        Initialize a new Song instance and update class statistics.

        Args:
            name (str): The name of the song.
            artist (str): The artist of the song.
            genre (str): The genre of the song.
        """
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update all class-level tracking
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count by one."""
        cls.count += 1

    def add_to_genres(self):
        """Add the song's genre to the genres list if not already present."""
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        """Add the song's artist to the artists list if not already present."""
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        """Increment the count for this song's genre."""
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        """Increment the count for this song's artist."""
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1