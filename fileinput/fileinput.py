#!/usr/bin/env python
import glob
from os import path

__metacass__ = type

BUFFER_SIZE = 1024 * 8

class fileinput:
	def __init__(self, fileLst = []):
		self.fileLst = fileLst
		self._fileLineNo = 0
		
	def setFiles(self, fileLst):
		self.fileLst = fileLst
	
	def getFiles(self):
		return self.fileLst
	
	def getFileNames(self):
		fileNameLst = list()
		for file in self.fileLst:
			 fileNameLst.append(path.basename(file))
		return fileNameLst
	
	def closeFiles(self, fileLst):
		'''
		Close all opened files.
		'''
		for file in self.fileLst:
			file.close()
			
	def getAllFiles(self, iterFiles, mode = r'r'):
		'''
		Get all the files.
		'''
# 		self.fileLst = list()
		try:
			for file in iterFiles:
				f = open(file, mode)
				self.fileLst.append(f)
			return self.fileLst
		except TypeError, e:
			for errorLine in e:
				if errorLine.find("Error"):
					print errorLine
					print "Please input iterable file list"
		except IOError, e:
			print e
			if errorLine.find("Error"):
					print errorLine
			self.closeFiles(self.fileLst)
			
	def fileno(self):
		pass
		
if __name__ == "__main__":
	file_path = r'C:\GitHub\fileInputAY-python\testFileInput\*.txt'
	fi = fileinput(glob.glob(file_path))
#	fi.setFiles(glob.glob(file_path))
	print fi.getFileNames()
	
	