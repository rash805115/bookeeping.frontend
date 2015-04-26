import abc

class Storage(metaclass = abc.ABCMeta):
	@abc.abstractmethod
	def inhale(self, localpath, remotepath):
		"""Copy file at localpath from local machine to remotepath at storage."""
		return
	
	@abc.abstractmethod
	def exhale(self, remotepath, localpath):
		"""Copy file from remotepath at storage to localpath at local machine."""
		return
	
	@abc.abstractmethod
	def potty(self, remotepath):
		"""Delete file from remotepath at storage."""
		return