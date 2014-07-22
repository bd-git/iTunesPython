import win32com.client
import shutil
import os
import inspect
import difflib
import pickle
import datetime

itunes = win32com.client.Dispatch('iTunes.Application')

mainLibrarySource   = itunes.LibrarySource
win32com.client.sys

playlists = mainLibrarySource.Playlists #Get Playlists currently in iTunes
libraryTracks = playlists.Item(1).Tracks #Playlist 1 is "Library", get all of its items (tracks)
numLibraryTracks = libraryTracks.Count #Get number of tracks in "Library"


libList = []
libDict = {}
count = 0
count2 = numLibraryTracks
print "Building Library"
while numLibraryTracks != 0:
    item = {} #initialize an empty dictionary
    song = libraryTracks.Item(numLibraryTracks) #get the current song
    item['fileName']=song.Location.split("\\")[-1] #split file location based on \, append last in list (ie SongName.mp3)
    item['filePath']=song.Location #the whole file dir
    item['newFilePath']=song.Location.replace("E:\\Music","\\\\nas\\media\\Music")
    #print item['newFilePath']
    item['rating']=song.Rating
    item['title']=song.Name
    item['comment']=datetime.datetime.fromtimestamp(int(song.DateAdded)) #PYTIME->DATETIME
    item['playedCount']=song.PlayedCount

    key = song.Artist+song.Name
    libDict[key]=item
    numLibraryTracks-=1

print "Done Building, Dumping to Pickle"

pickleOut = open('iTunesLibraryTransfer.pickle','wb')
pickle.dump(libDict, pickleOut)
libDict=[]
pickleOut.close()

print "Done Pickleing"




