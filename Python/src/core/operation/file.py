class File:
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