#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 26, 2018 06:03:57 PM
#    May 26, 2018 06:06:23 PM


import sys
import lyrics
from genius import Genius
from Spotify import *

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



def btnGoClick(p1, title, artist):
	#Title ed artist sono StringVar, get consente di prendere la stringa
    title = title.get()
    artist = artist.get()
    if not title and not artist:
        print("Inserisci il titolo e l'artista prima")
    else:
        song = Genius.getLyrics(title, artist)
        print(song)
        destroy_window()
        input("\n\n\n\n\tPremi invio per uscire")
    sys.stdout.flush()

def spotifyLabelClick(p1):
    if Spotify().isSpotifyPlaying:
        song = Spotify().currentSong
        l = Genius.getLyrics(song.title, song.artist)
        print(l)
        destroy_window()
        input("\n\n\n\n\tPremi invio per uscire")
    sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    lyrics.vp_start_gui()