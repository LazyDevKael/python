import subprocess

def OpenTextEdit():
	subprocess.call(["/usr/bin/open", "-a", "/Applications/TextEdit.app"])

def OpenMPlayerX():
	subprocess.call(["/usr/bin/open", "-a", "/Applications/MPlayerX.app"])

def OpenTextFile(file):
	subprocess.call(["/usr/bin/open", "-a", "/Applications/TextEdit.app", file])

def OpenVideo(video):
	subprocess.call(["/usr/bin/open", "-a", "/Applications/MPlayerX.app", video])

