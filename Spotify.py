from time import sleep
import dbus
class Spotify:

    def __init__(self):
        try:
            self.spotify_bus = dbus.SessionBus().get_object("org.mpris.MediaPlayer2.spotify",
                "/org/mpris/MediaPlayer2")
        except:
            self.isSpotifyPlaying = False
        else:
            self.isSpotifyPlaying = True
        if self.isSpotifyPlaying:
            self.spotify_properties = dbus.Interface(self.spotify_bus,"org.freedesktop.DBus.Properties")
            self.spotify_player = dbus.Interface(self.spotify_bus, "org.mpris.MediaPlayer2.Player")
            self.metadata = self.spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
            self.currentSong = self.to_song()
        else:
            self.currentSong="Spotify is not playing anything"

    def update_song(self):
        if self.isSpotifyPlaying:
            self.metadata = self.spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
            self.currentSong = self.to_song()
            return self
        else:
            self.currentSong="Spotify is not playing anything"

    def to_song(self):
        if self.isSpotifyPlaying:
            album = str(self.metadata["xesam:album"])
            artist = str(self.metadata["xesam:artist"][0].strip())
            title = str(self.metadata["xesam:title"])
            spotifyURL = str(self.metadata["xesam:url"])
            return Song(title, artist, spotifyURL, album)

    def PlayPause(self):
        if self.isSpotifyPlaying:
            self.spotify_player.PlayPause()

    def Next(self):
        if self.isSpotifyPlaying:
            self.spotify_player.Next()
            sleep(0.5)
            self.update_song()
    def Previous(self):
        if self.isSpotifyPlaying:
            self.spotify_player.Previous()
            sleep(0.5)
            self.update_song()

class Song:
    def __init__(self, title, artist, spotifyURL="", album=""):
        self.title = title
        self.artist = artist
        self.album = album
        self.spotifyURL = spotifyURL
    def __str__(self):
        return f"""\
Album: {self.album}
Artist: {self.artist}
Title: {self.title}
Spotify URL: {self.spotifyURL}"""
    def __repr__(self):
        return "repr: \n" + self.__str__()

if __name__ == "__main__":
    print(Spotify().currentSong)
