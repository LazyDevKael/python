
from FileSystemService import FileSystemService

fs = FileSystemService()
print("\n".join(fs.getAll("D:\workspace\github\python\WebFileExplore\source")))
print()
print("\n".join(fs.getAllFiles("D:\workspace\github\python\WebFileExplore\source")))

