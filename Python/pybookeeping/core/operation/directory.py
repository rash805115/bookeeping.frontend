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
		
		try:
			response = self._connection.post_request("directory/info", str(payload))
			return True, response["data"]
		except ValueError as error:
			return False, error.args[0]["operation_message"]
	
	def modify_directory(self, nodeid, properties = {}):
		payload = {
			"nodeId": nodeid
		}
		payload.update(properties)
		
		try:
			response = self._connection.post_request("node/modify", str(payload))
			return True, response
		except ValueError as error:
			return False, error.args[0]["operation_message"]
	
	def create_directory(self, commit, user_id, filesystem_id, filesystem_version, directory_path, directory_name, properties = {}):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"directoryPath": directory_path,
			"directoryName": directory_name
		}
		sub_payload.update(properties)
		commit.add_event({"DIRECTORY_CREATE": sub_payload})
	
	def create_directory_version(self, commit, node_id, change_metadata, properties = {}):
		sub_payload = {
			"nodeId": node_id,
			"CHANGE_METADATA": change_metadata
		}
		sub_payload.update(properties)
		commit.add_event({"NODE_VERSION": sub_payload})
	
	def delete_directory(self, commit, node_id):
		sub_payload = {
			"nodeId": node_id
		}
		commit.add_event({"NODE_DELETE": sub_payload})
	
	def restore_directory(self, commit, user_id, filesystem_id, filesystem_version, directory_path, directory_name, node_id_to_be_restored):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"directoryPath": directory_path,
			"directoryName": directory_name,
			"nodeIdToBeRestored": node_id_to_be_restored
		}
		commit.add_event({"DIRECTORY_RESTORE": sub_payload})
	
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
		commit.add_event({"DIRECTORY_MOVE": sub_payload})