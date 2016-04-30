#!/usr/bin/env python
import glob
from os import path

__metacass__ = type

ALLOWED_MODE_LIST = ('r', 'rU', 'U', 'rb')

class fileinput:
	def __init__(self, fileLst = [], mode = r'r'):
		self.fileLst = fileLst
		self._current_file_name = ""
		self.mode = mode
		self._file_line_no = 0
		self._file_no = 0

	def __enter__(self):
		pass
	
	def __exit__(self, type, value, trace):
		self._closeFiles(self.fileLst)
	
	def setFiles(self, fileLst):
		self.fileLst = fileLst
	
	def getFiles(self):
		return self.fileLst
	
	def _getFileNames(self):
		fileNameLst = list()
		for file in self.fileLst:
			 fileNameLst.append(path.basename(file))
		return fileNameLst
	
	def _closeFiles(self, opened_file_lst):
		'''
		Close all opened files.
		'''
		try:
			if type(opened_file_lst) is str:
				opened_file_lst.close()
			else:
				for file in self.opened_file_lst:
					file.close()
		except Exception, e:
			pass
				
	def _currentOpenFiles(self, file, mode = r'r'):
		'''
		Get current file.
		Only mode 'r', 'rU', 'U', 'rb' are allowed. Otherwise exception FileModeError will be raised
		'''
		
		if mode not in ALLOWED_MODE_LIST:
			mode_str = ""
			for mode_item in ALLOWED_MODE_LIST:
				mode_str += "%s, "
			error_msg = "FileModeError: Please input correct open file mode: (" + mode_str.rstrip(", ") + ")"
			raise Exception(error_msg % ALLOWED_MODE_LIST)
		
		try:
			__f = open(file, mode)
			self._current_file_name = path.basename(file)
			return __f
		except IOError, e:
			for errorLine in e:
				if errorLine.find("Error"):
					print errorLine
			self._closeFiles(self.fileLst)
	
	def getLines(self):
		for file in self.fileLst:
			self._file_no += 1
			try:
				for line in self._currentOpenFiles(file, self.mode):
					self._file_line_no += 1
					yield line
			except IOError, e:
				print e
			finally:
				self._closeFiles(file)
				
	def getFileName(self):
		return self._current_file_name
				
	def _getAllFiles(self, iterFiles, mode = r'r'):
		'''
		Get all the files.
		'''
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
			for errorLine in e:
				if errorLine.find("Error"):
					print errorLine
			self._closeFiles(self.fileLst)
			
	def fileNo(self):
		return self._file_no
	
	def fileLineNo(self):
		return self._file_line_no
	
	def getFileNames(self):
		return self._getFileNames()
		
if __name__ == "__main__":
	file_path = r'C:\GitHub\fileInputAY-python\testFileInput\*.txt'
	fi = fileinput(glob.glob(file_path), r'r')
#	fi.setFiles(glob.glob(file_path))
	for file in fi.getFileNames():
		print file
# 	fi.currentOpenFiles('abc', 'aa')

	for line in fi.getLines():
		print "File No.%d, File Name: %s, Line No.%d. File Content: %s" % (fi.fileNo(), fi.getFileName(), fi.fileLineNo(), line)
	
	
	
	