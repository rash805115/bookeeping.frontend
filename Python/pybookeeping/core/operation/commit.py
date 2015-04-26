class Commit:
	def __init__(self, connection, commit_id):
		self._connection = connection
		
		self.payload = {
			"commitId": commit_id
		}
	
	def commit(self):
		response = self._connection.request("commit", self.payload)
		self._connection = None
		return response