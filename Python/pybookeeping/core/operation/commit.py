class Commit:
	def __init__(self, connection, commit_id):
		self._connection = connection
		self._next_commit_sequence = 0
		
		self._payload = {
			"commitId": commit_id
		}
	
	def add_event(self, payload):
		self._payload[self._next_commit_sequence] = payload
		self._next_commit_sequence = self._next_commit_sequence + 1
	
	def commit(self):
		response = self._connection.request("commit", self._payload)
		self._connection = None
		return response["data"]