class Filesystem:
	def __init__(self, connection):
		self._connection = connection
	
	def get_filesystem(self, user_id, filesystem_id):
		payload = {
			"userId": user_id,
			"filesystemId": filesystem_id
		}
		return self._connection.request("filesystem/info", payload)
	
	def create_filesystem(self, commit, user_id, filesystem_id):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id
		}
		commit.payload.update({"Filesystem_Create": sub_payload})