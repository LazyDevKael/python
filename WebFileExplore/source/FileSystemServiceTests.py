
from FileSystemService import FileSystemService

fs = FileSystemService()
print("The content of D:\workspace\github\python\WebFileExplore\source is:")
print("\n".join(fs.getAll("D:\workspace\github\python\WebFileExplore\source")))
print()
print("Files in D:\workspace\github\python\WebFileExplore\source are:")
print("\n".join(fs.getAllFiles("D:\workspace\github\python\WebFileExplore\source")))
print()
print("Directories in D:\workspace\github\python\WebFileExplore\source are:")
print("\n".join(fs.getAllDirectories("D:\workspace\github\python\WebFileExplore\source")))
