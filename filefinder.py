#!/usr/bin/env python3

import sys
import os


arguments = sys.argv

counter = 0

if len(arguments) == 3:
        searchPath = arguments[1]
        extension = arguments[2]

        if os.path.isdir(searchPath):

                for CurDir,SubDir,SubFiles in os.walk(searchPath):
                        for subfile in SubFiles:
                                abPath = os.path.join(CurDir,subfile)
                                if abPath.endswith(extension):
                                        print( ': {}'.format(abPath) )
                                        counter = counter + 1
                print( 'Total : {}'.format(counter) )
        else:
                print('')
                print("Directory {} not found".format(searchPath))
                print('')

else:
        print('')
        print('Usage : filefinder  Path  Extension')
        print('')
