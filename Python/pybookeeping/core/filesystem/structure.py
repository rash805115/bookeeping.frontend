import hashlib
import os
import threading

class Structure:
	def __init__(self, rootdirectory):
		self._rootdirectory = rootdirectory[0 : -1] if rootdirectory[-1] == "/" else rootdirectory
	
	def absolutepath(self, relativepath):
		if(relativepath == ""):
			return self._rootdirectory
		
		relativepath = relativepath[1 : ] if(relativepath[0] == "/") else relativepath
		path = self._rootdirectory + "/" + relativepath
		return path[0 : -1] if(path[-1] == "/") else path
	
	def stringhash(self, string):
		return hashlib.md5(string.encode("UTF-8")).hexdigest()
	
	def filehash(self, filepath):
		fileHash = hashlib.md5()
		with open(filepath, "rb") as file:
			while(True):
				chunk = file.read(2**10)
				if not chunk:
					break
				
				fileHash.update(chunk)
			
		return fileHash.hexdigest()
	
	def filesummary(self, filepath):
		filename = filepath[filepath.rfind("/") + 1 : ]
		relative_filepath = filepath[len(self._rootdirectory) : ]
		namehash = self.stringhash(filename)
		contenthash = self.filehash(filepath)
		combinedhash = self.stringhash(namehash + contenthash)
		
		filesummary = {
			"namehash": namehash,
			"contenthash": contenthash,
			"combinedhash": combinedhash,
			"directory": False,
			"name": filename,
			"path": "/" if relative_filepath[ : relative_filepath.rfind("/")] == "" else relative_filepath[ : relative_filepath.rfind("/")],
			"children": "none" 
		}
		
		return filesummary
	
	def directorysummary(self, directorypath, childrentree):
		directoryname = directorypath[directorypath.rfind("/") + 1 : ]
		relative_dirpath = directorypath[len(self._rootdirectory) : ]
		directoryhash = hashlib.md5()
		
		for key in sorted(childrentree.keys()):
			directoryhash.update(childrentree[key]["combinedhash"].encode("UTF-8"))
		
		namehash = self.stringhash(directoryname)
		contenthash = directoryhash.hexdigest()
		combinedhash = self.stringhash(namehash + contenthash)
		
		directorysummary = {
			"namehash": namehash,
			"contenthash": contenthash,
			"combinedhash": combinedhash,
			"directory": True,
			"name": directoryname,
			"path": "/" if relative_dirpath[ : relative_dirpath.rfind("/")] == "" else relative_dirpath[ : relative_dirpath.rfind("/")],
			"children": childrentree
		}
		
		return directorysummary
	
	def bonelevels(self, relativepath):
		bonelevels = []
		directorypath = self.absolutepath(relativepath)
		
		maxlevel = -1
		for root, _, _ in os.walk(directorypath):
			level = root.replace(directorypath, "").count("/")
			if(level <= maxlevel):
				bonelevels[level] += [(root + "/" + i) for i in os.listdir(root)]
			else:
				maxlevel = level
				bonelevels.append([(root + "/" + i) for i in os.listdir(root)])
		
		return bonelevels
	
	def _bonescan(self, bonelevel, previous_level_dictionary, current_level_dictionary):
		while(len(bonelevel) > 0):
			path = bonelevel.pop(0)
			if(os.path.isdir(path)):
				childrentree = {}
				for key in previous_level_dictionary.keys():
					if key.startswith(path[len(self._rootdirectory) : ]):
						childrentree[key] = previous_level_dictionary[key]
				
				summary = self.directorysummary(path, childrentree)
			else:
				summary = self.filesummary(path)
			
			current_level_dictionary.update({path[len(self._rootdirectory) : ]: summary})
	
	def xray(self, relativepath):
		bonelevels = self.bonelevels(relativepath)
		previous_level_dictionary = {}
		current_level_dictionary = {}
		
		thread_workload = 10
		for level in reversed(bonelevels):
			threadcount = int(len(level) / thread_workload) + 1
			threads = []
			
			for _ in range(threadcount):
				bonescan_thread = threading.Thread(target = self._bonescan, args = (level, previous_level_dictionary, current_level_dictionary))
				threads.append(bonescan_thread)
			
			[thread.start() for thread in threads]
			[thread.join() for thread in threads]
			
			previous_level_dictionary = current_level_dictionary
			current_level_dictionary = {}
		
		return previous_level_dictionary