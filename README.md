iTunesPython
============

Python scripts to manage iTunes

===========


iTunes Pickler:

This is useful if you need to reinstall iTunes (or specifically, Windows)
and MOST USEFUL if you need to do a mass directory change.
For example:
*>Old PC Music: E:\music
*>New PC fresh install iTunes, music on new PC is: F:\music
-->Run iTunes pickler on old PC to pull out info you want to keep, put what new location will be
-->Install iTunes on new PC, open iTunes, drag all music into iTunes (from new location)
-->Library will be blank (no play counts, ratings)
-->Run unPickler to initialize new iTunes library



iTunes UnPickler_andLoader:

See use case from above



trashOneStar:

My iTunes is set such that all 1star songs should be removed. I only want to keep unrated and 2+Star.
I don't want the Songs that are removed from iTunes to stay in my PC's music folder,
but I also don't necessarily want to delete them. Move to 'trash' location.



similarAlbums:

iPods/iPhones or other mp3 players or music managers will initialize their libraries based on your info. 
Everyone knows how frustrating it is when an Artist has 10+ 1-song albums because of typos.
For example, ACDC\TNT\Song1.mp3 and ACDC\TnT\Song2.mp3 <---2 different albums.
This script should list albums like that (finds some false positives, too).



