import plugins.storage.interface.storage
import boto.s3.connection
import boto.s3.key

class AmazonS3(plugins.storage.interface.storage.Storage):
	def __init__(self, accesskey, secretkey, bucketname):
		self._connection = boto.s3.connection.S3Connection(accesskey, secretkey)
		self._bucket = self._connection.get_bucket(bucketname)
		self._key = boto.s3.key.Key(self._bucket)
	
	def inhale(self, localpath, remotepath):
		self._key.key = remotepath
		self._key.set_contents_from_filename(localpath)
	
	def exhale(self, remotepath, localpath):
		self._key.key = remotepath
		self._key.get_contents_to_filename(localpath)
	
	def potty(self, remotepath):
		self._key.key = remotepath
		self._key.delete()