import win32com.client
import shutil
import os

itunes = win32com.client.Dispatch('iTunes.Application')

mainLibrarySource   = itunes.LibrarySource
win32com.client.sys

playlists = mainLibrarySource.Playlists #Get Playlists currently in iTunes
libraryTracks = playlists.Item(1).Tracks #Playlist 1 is "Library"
numLibraryTracks = libraryTracks.Count #Get number of tracks in "Library"

print numLibraryTracks , "Songs\nScanning Library..."

count = 0
while numLibraryTracks != 0:
        song = libraryTracks.Item(numLibraryTracks)
        src = song.Location
        
        if song.Rating == 20: #if song rating is 1 star...
                dst="Z:\\Other Music\\TrashedMusic\\"
                if not(src == ''): #if song not 'unfindable' by iTunes...
                        shutil.copy2(src,dst)
                        print "\ttrash ", song.Artist , " - " , song.Name
                        song.Delete()
                        os.remove(src)
                        count+=1
 
         
        numLibraryTracks-=1

print count, "Deleted from iTunes+PC (moved to trash)"

