def print_directory_path(sPath):
	import os
	for childFileName in os.listdir(sPath):
		childPath = os.path.join(sPath, childFileName)
		if os.path.isdir(childPath):
			print_directory_path(childPath)
		else:
			print childPath


print_directory_path("E:\git_project")
