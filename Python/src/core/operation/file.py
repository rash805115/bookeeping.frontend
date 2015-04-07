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
		return self._connection.request("file/info", payload)
	
	def create_file(self, commit, user_id, filesystem_id, filesystem_version, file_path, file_name):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"filePath": file_path,
			"fileName": file_name
		}
		commit.payload.update({"File_Create": sub_payload})
	
	def create_file_version(self, commit, node_id):
		sub_payload = {
			"nodeId": node_id
		}
		commit.payload.update({"Node_Version": sub_payload})
	
	def delete_file(self, commit, node_id):
		sub_payload = {
			"nodeId": node_id
		}
		commit.payload.update({"Node_Delete": sub_payload})
	
	def restore_file(self, commit, user_id, filesystem_id, filesystem_version, file_path, file_name, node_id_to_be_restored):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"filePath": file_path,
			"fileName": file_name,
			"nodeIdToBeRestored": node_id_to_be_restored
		}
		commit.payload.update({"File_Restore": sub_payload})
	
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
		commit.payload.update({"File_Move": sub_payload})
	
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
		commit.payload.update({"File_Share": sub_payload})
	
	def unshare_file(self, commit, user_id, filesystem_id, filesystem_version, file_path, file_name, unshare_with_user):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"filePath": file_path,
			"fileName": file_name,
			"shareWithUserId": unshare_with_user
		}
		commit.payload.update({"File_Unshare": sub_payload})