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
		return self._connection.request("directory/info", payload)
	
	def create_directory(self, commit, user_id, filesystem_id, filesystem_version, directory_path, directory_name):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"filesystemVersion": filesystem_version,
			"directoryPath": directory_path,
			"directoryName": directory_name
		}
		commit.payload.update({"Directory_Create": sub_payload})