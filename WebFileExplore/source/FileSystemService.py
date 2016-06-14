from os import listdir
from os.path import isfile, join

class FileSystemService:

	def getAll(self, path):
		return listdir(path)

	def getAllFiles(self, path):
		return [name for name in listdir(path) if isfile(join(path, name))]

	def getAllDirectories(self, path):
		return [name for name in listdir(path) if not isfile(join(path, name))]

	def isSubDirectory(self, parentPath, childPath):
		return childPath in getAllDirectories(parentPath)

	def getParentDirectory(self):
		return ".."


