class Song:
    def __init__(self, artist, title, duration):
        self.artist = artist
        self.title = title
        self.duration = duration

class Album:
    def __init__(self, title):
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

class MusicLibrary:
    def __init__(self):
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def get_songs_by_artist(self, artist_name):
        songs_by_artist = []
        for album in self.albums:
            for song in album.songs:
                if song.artist == artist_name:
                    songs_by_artist.append((song.title, album.title))
        return songs_by_artist

# Example usage
# Create a song
if __name__ == '__main__':
    song1 = Song("Artist1", "Song Title 1", 240)

    # Create an album and add the song
    album1 = Album("Album Title 1")
    album1.add_song(song1)

    # Create a music library, add the album, and retrieve songs by artist
    library = MusicLibrary()
    library.add_album(album1)
    artist_songs = library.get_songs_by_artist("Artist1")
