import os
import path
import shutil
from MovieSerieTorrent import Parser

DIRECTORY = ''
COMPLETED = ''
FILETYPES = ['*.avi','*.mkv', '*.mov', '*.mp4', '*.wmv', '*.AVI' '*.MKV', '*.MOV', '*.MP4', '*.WMV']
d = path.Path(DIRECTORY)
c = path.Path(COMPLETED)

if not d.exists() and not c.exists():
    d.touch()
    c.touch()

for f in d.walkfiles():
    # Loop through each type in FILETYPE to check for matches
    for ftype in FILETYPES:
        # If the file type is a video file, then...
        if f.fnmatch(ftype):
            # Parse the name of the file with MovieSerieTorrent
            p = Parser().parse(f.basename())[0]
            if p['type'] == 'serie' and 'season' in p:
                # Define the name of the new directory and file
                dirname = '{}{}/{}'.format(COMPLETED, p['title'], p['season'])
                epname = '.'.join([p['title'], p['season'], p['episode']]) + f.name[-4:]
                print 'Moving {} from directory {} to directory {}...'.format(f.name, f.dirname(), dirname)
                # Create new directory if it doesn't exist
                if not path.Path(dirname).exists():
                    print dirname, 'does not exist, creating directory...'
                    os.makedirs(dirname)
                # Define destination file
                ftest = '{}/{}'.format(dirname, f.name)
                # If destination file doesn't exist, move to destination
                if not path.Path(ftest).exists():
                    shutil.move(f, dirname)
                    os.rename(ftest, dirname + '/' + epname)
                elif path.Path(ftest).exists():
                    print 'File already exists...'
                else:
                    print 'Unknown error, moving file to destination anyway...'
                    shutil.move(f, dirname)
                    os.rename(ftest, dirname + '/' + epname)

            elif p['type'] =='movie' or 'season' not in p:
                # "Season not in p" will trigger essentially any file if not caught by FILETYPES, may cause errors in defining movname and dirname
                # Define the name of the new directory and file
                movname = '{} ({})'.format(p['title'], p['year']) + f.name[-4:]
                dirname = COMPLETED + '{} ({})'.format(p['title'], p['year'])
                # Create directory if it doesn't already exist
                if not path.Path(dirname).exists():
                    # Print dirname, 'does not exist, creating directory...'
                    os.makedirs(dirname)
                # Define destination file
                ftest = '{}/{}'.format(dirname, f.name)
                # If destination file doesn't exist, move to destination
                if not path.Path(ftest).exists():
                    shutil.move(f, dirname)
                    os.rename(ftest, dirname + '/' + movname)
                elif path.Path(ftest).exists():
                    print 'File already exists...'
                else:
                    print 'Unknown error, moving file to destination anyway...'
                    shutil.move(f, dirname)
                    os.rename(ftest, dirname + '/' + movname)
        else:
            pass
