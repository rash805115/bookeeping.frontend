class File:
	WRITE_PERMISSION = "write"
	READ_PERMISSION = "read"
	
	def __init__(self, connection):
		self._connection = connection
	
	def get_file(self, user_id, filesystem_id, filesystem_version, file_path, file_name):
		payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"filePath": file_path,
			"fileName": file_name
		}
		
		try:
			response = self._connection.post_request("file/info", str(payload))
			return True, response["data"]
		except ValueError as error:
			return False, error.args[0]["operation_message"]
	
	def modify_file(self, nodeid, properties = {}):
		payload = {
			"nodeId": nodeid
		}
		payload.update(properties)
		
		try:
			response = self._connection.post_request("node/modify", str(payload))
			return True, response
		except ValueError as error:
			return False, error.args[0]["operation_message"]
	
	def create_file(self, commit, user_id, filesystem_id, filesystem_version, file_path, file_name, properties = {}):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"filePath": file_path,
			"fileName": file_name
		}
		sub_payload.update(properties)
		commit.add_event({"FILE_CREATE": sub_payload})
	
	def create_file_version(self, commit, node_id, change_metadata, properties = {}):
		sub_payload = {
			"nodeId": node_id,
			"CHANGE_METADATA": change_metadata
		}
		sub_payload.update(properties)
		commit.add_event({"NODE_VERSION": sub_payload})
	
	def delete_file(self, commit, node_id):
		sub_payload = {
			"nodeId": node_id
		}
		commit.add_event({"NODE_DELETE": sub_payload})
	
	def restore_file(self, commit, user_id, filesystem_id, filesystem_version, file_path, file_name, node_id_to_be_restored):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"filePath": file_path,
			"fileName": file_name,
			"nodeIdToBeRestored": node_id_to_be_restored
		}
		commit.add_event({"FILE_RESTORE": sub_payload})
	
	def move_file(self, commit, user_id, filesystem_id, filesystem_version, old_file_path, old_file_name, new_file_path, new_file_name):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"oldFilePath": old_file_path,
			"oldFileName": old_file_name,
			"newFilePath": new_file_path,
			"newFileName": new_file_name
		}
		commit.add_event({"FILE_MOVE": sub_payload})
	
	def share_file(self, commit, user_id, filesystem_id, filesystem_version, file_path, file_name, share_with_user, file_permission):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"filePath": file_path,
			"fileName": file_name,
			"shareWithUserId": share_with_user,
			"filePermission": file_permission
		}
		commit.add_event({"FILE_SHARE": sub_payload})
	
	def unshare_file(self, commit, user_id, filesystem_id, filesystem_version, file_path, file_name, unshare_with_user):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"filePath": file_path,
			"fileName": file_name,
			"shareWithUserId": unshare_with_user
		}
		commit.add_event({"FILE_UNSHARE": sub_payload})