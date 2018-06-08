import os, sys
import lyricsgenius
import argparse

parser = argparse.ArgumentParser(description="Get lyrics of the current song playing (via Spotify) from genius.com, if title and artist are submitted via arguments then the program will return the lyrics of that song.")
parser.add_argument("--title", required=False, nargs=1)
parser.add_argument("--artist", required=False, nargs=1)

class HiddenPrints:
    #Ho preso spunto da una risposta su StackOverflow :)
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = None

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self._original_stdout


class Genius:
    api = lyricsgenius.Genius("Pn1OMztO32zbScpe1K8mTcmELOqmMSQL_aElU9I8pkjUyDZg7AAcmOf01PwnmT5g")
    @classmethod
    def getLyrics(cls, title=None, artist=None, song=None):
        if title==None and artist==None and song!=None and type(song) == Song:
            title = song.title
            artist = song.artist
        try:
            with HiddenPrints():
                return cls.api.search_song(title, artist).lyrics
        except:
            try:
                with HiddenPrints():
                    return cls.api.search_song(title.split("(")[0], artist).lyrics
            except:
                try:
                    with HiddenPrints():
                        return cls.api.search_song(title.split("feat")[0], artist).lyrics
                except:
                    try:
                        with HiddenPrints():
                            return cls.api.search_song(title.split("ft.")[0], artist).lyrics
                    except:
                        pass
        return "Lyrics not found :/"

if __name__ == "__main__":
    import Spotify as sp
    songToFind = sp.Song("", "")
    try:
        args = parser.parse_args()
        if args is not None:
            if args.artist is not None:
                songToFind.artist = args.artist[0]
            if args.title is not None:
                songToFind.title = args.title[0]
        if songToFind.artist == "" and songToFind.title == "":
            songToFind = sp.Spotify().currentSong
    except:
        pass
    print(Genius.getLyrics(songToFind.title, songToFind.artist))
