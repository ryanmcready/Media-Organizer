## Media Organizer

[Plex](https://www.plex.tv/) has a specific folder structure that it likes. When downloading multiple season packs for series, it can be time consuming moving episodes out of their own individual folders. This script analyzes video files and puts them in the following format:
- /COMPLETED directory name
  - /TV Show Example
    - /S01
      - TV Show Example.S01.E01.mp4
      - TV Show Example.S01.E02.mp4
    - /S02
      - TV Show Example.S02.E01.mp4
  - /Movie (year)
    - Movie (year).mkv

### Usage:
- Set your DIRECTORY and COMPLETED variables.
  - *DIRECTORY* = Folder that your downloads are in. This is the folder the script will organize the media from.
  - *COMPLETED* = Folder sorted media will be placed in.
- The *FILETYPES* shouldn't need to be changed, but if you are working with other video files you can add them to the list. Make sure you use the wildcard symbol (\*) when you add them.

**Important:** Make sure your COMPLETED folder is not a subdirectory of DIRECTORY. This will prevent media already sorted from being parsed again.

Notes:
This script uses MovieSerieTorrent to parse through file names. Movies will occasionally get labeled as series, but I have added in an additional check to try to prevent this. This shouldn't be a problem as they all get moved to the *COMPLETED* directory regardless of type.

Requirements:

[path.py](https://github.com/jaraco/path.py)

[MovieSerieTorrent](https://github.com/JonathanPetit/MovieSerieTorrent)
