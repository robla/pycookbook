#!/usr/bin/env python3
import os

def sloppymkdir(dirname):
    try:
        os.mkdir(dirname)
    except FileExistsError:
        print('You have ' + dirname + ' already')

sloppymkdir('/tmp/f1')
sloppymkdir('/tmp/f1/targ1')
sloppymkdir('/tmp/f1/tags-repo')

# targetvalue where the symlink will be pointing to
# It may be a relative or absolute path.  In the UNIX way of thinking,
# this is the "src"
symlinkvalue = '../targ1'

# symlinkfilename is the name of the resulting file on disk.  In the
# the UNIX way of thinking, this is the "dest"
symlinkfilename = 'pointer-to-targ1'

# symlinkdir is where the symlink is actually going to be stored
symlinkdir = '/tmp/f1/tags-repo'

# dir_fd is the current working directory as far as this program is 
# concerned.  It needs to be a file handle, but can probably be a read
# only file handle (so os.O_RDONLY may also work if that's needed on 
# platforms that don't support os.O_DIRECTORY)
symlinkdir_fd = os.open(symlinkdir, os.O_DIRECTORY)

try:
    os.symlink(symlinkvalue, symlinkfilename, dir_fd=symlinkdir_fd)
except FileExistsError:
    print('You have ' + symlinkfilename + ' already')


# The result:
#  /tmp/f1/tags-repo$ ls -l
# total 0
# lrwxrwxrwx. 1 robla robla 8 2017-10-03 13:15 pointer-to-targ1 -> ../targ1


