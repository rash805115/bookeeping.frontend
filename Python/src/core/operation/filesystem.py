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
	
	def create_filesystem_version(self, commit, node_id):
		sub_payload = {
			"nodeId": node_id
		}
		commit.payload.update({"Node_Version": sub_payload})
	
	def delete_filesystem(self, commit, node_id):
		sub_payload = {
			"nodeId": node_id
		}
		commit.payload.update({"Node_Delete": sub_payload})
	
	def restore_filesystem(self, commit, user_id, filesystem_id, node_id_to_be_restored):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"nodeIdToBeRestored": node_id_to_be_restored
		}
		commit.payload.update({"Filesystem_Restore": sub_payload})