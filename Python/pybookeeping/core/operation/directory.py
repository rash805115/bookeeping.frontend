class Directory:
	def __init__(self, connection):
		self._connection = connection
	
	def get_directory(self, user_id, filesystem_id, filesystem_version, directory_path, directory_name):
		payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"directoryPath": directory_path,
			"directoryName": directory_name
		}
		response = self._connection.request("directory/info", payload)
		return response["data"]
	
	def create_directory(self, commit, user_id, filesystem_id, filesystem_version, directory_path, directory_name):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"directoryPath": directory_path,
			"directoryName": directory_name
		}
		commit.payload.update({"Directory_Create": sub_payload})
	
	def create_directory_version(self, commit, node_id):
		sub_payload = {
			"nodeId": node_id
		}
		commit.payload.update({"Node_Version": sub_payload})
	
	def delete_directory(self, commit, node_id):
		sub_payload = {
			"nodeId": node_id
		}
		commit.payload.update({"Node_Delete": sub_payload})
	
	def restore_directory(self, commit, user_id, filesystem_id, filesystem_version, directory_path, directory_name, node_id_to_be_restored):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"directoryPath": directory_path,
			"directoryName": directory_name,
			"nodeIdToBeRestored": node_id_to_be_restored
		}
		commit.payload.update({"Directory_Restore": sub_payload})
	
	def move_directory(self, commit, user_id, filesystem_id, filesystem_version, old_directory_path, old_directory_name, new_directory_path, new_directory_name):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"oldDirectoryPath": old_directory_path,
			"oldDirectoryName": old_directory_name,
			"newDirectoryPath": new_directory_path,
			"newDirectoryName": new_directory_name
		}
		commit.payload.update({"Directory_Move": sub_payload})