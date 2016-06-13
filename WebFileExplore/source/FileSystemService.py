
from os import listdir
from os.path import isfile

class FileSystemService:

	def getAll(self, path):
		return listdir(path)

fs = FileSystemService()
print("\n".join(fs.getAll("D:\workspace\github")))
