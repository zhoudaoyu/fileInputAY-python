'''
Created on Apr 29, 2016

@author: daoyu.zhou
'''

#!/usr/bin/env python

__metaclass__ = type

import glob 
import fileinput

class UseFileInput:
    def displayLines(self, files):
        for line in fileinput.input(files):
            print line
            
    def testGlob(self, path):
        print glob.glob(path)

if __name__ == '__main__':
    path = r'C:\GitHub\fileInputAY-python\testFileInput\*.txt'
    ufi = UseFileInput()
    ufi.displayLines(glob.glob(path))
    ufi.testGlob(path)