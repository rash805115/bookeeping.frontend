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
		try:
			response = self._connection.post_request("commit", str(self._payload))
			return True, response["data"]
		except ValueError as error:
			return False, error.args[0]["operation_message"]
		
		self._connection = None