import win32com.client
import shutil
import os
import inspect
import difflib

itunes = win32com.client.Dispatch('iTunes.Application')

mainLibrarySource   = itunes.LibrarySource
win32com.client.sys

playlists = mainLibrarySource.Playlists #Get Playlists currently in iTunes
libraryTracks = playlists.Item(1).Tracks #Playlist 1 is "Library", get all of its items (tracks)
numLibraryTracks = libraryTracks.Count #Get number of tracks in "Library"

albums = set()

while numLibraryTracks != 0:
    song = libraryTracks.Item(numLibraryTracks)
    albums.add(song.Album)
    numLibraryTracks-=1

z=[]

for x in albums:
    for y in albums:
        match = difflib.SequenceMatcher(None, x, y)       
        if match.ratio() < 1.0 and match.ratio() > 0.8:
            z.append(x)

z.sort()

for x in z:
    print x
        

