import win32com.client
import shutil
import os
import inspect
import difflib
import pickle
import datetime
import pywintypes

itunes = win32com.client.Dispatch('iTunes.Application')

mainLibrarySource   = itunes.LibrarySource
win32com.client.sys

playlists = mainLibrarySource.Playlists #Get Playlists currently in iTunes
libraryTracks = playlists.Item(1).Tracks #Playlist 1 is "Library", get all of its items (tracks)
numLibraryTracks = libraryTracks.Count #Get number of tracks in "Library"

libDict = pickle.load(open("iTunesLibraryTransfer.pickle",'rb'))

while numLibraryTracks != 0:
    song =libraryTracks.Item(numLibraryTracks)
    loc = song.Location
    try:
        for currentStoredSong in libDict.itervalues():
            if currentStoredSong['filePath']==loc:
                song.Rating=currentStoredSong['rating']
                song.PlayedCount=currentStoredSong['playedCount']
    except:
        print '\tEXCEPTION ',loc
    
    numLibraryTracks-=1

print 'Done'
