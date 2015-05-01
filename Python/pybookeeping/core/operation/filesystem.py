import pybookeeping.core.operation.user as user
import pybookeeping.core.operation.xray as xray

class Filesystem:
	def __init__(self, connection):
		self._connection = connection
	
	def get_filesystem(self, user_id, filesystem_id):
		payload = {
			"userId": user_id,
			"filesystemId": filesystem_id
		}
		response = self._connection.request("filesystem/info", payload)
		return response["data"]
	
	def get_all_filesystem(self, user_id):
		user_obj = user.User(self._connection)
		user_node = user_obj.get_user(user_id)["nodeId"]
		
		xray_obj = xray.Xray(self._connection)
		return xray_obj.xray_node(user_node)
	
	def create_filesystem(self, user_id, filesystem_id, local_path):
		payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"localPath": local_path
		}
		return self._connection.request("filesystem/create", payload)
	
	def create_filesystem_version(self, commit, node_id):
		sub_payload = {
			"nodeId": node_id
		}
		commit.add_event({"Node_Version": sub_payload})
	
	def delete_filesystem(self, commit, node_id):
		sub_payload = {
			"nodeId": node_id
		}
		commit.add_event({"Node_Delete": sub_payload})
	
	def restore_filesystem(self, commit, user_id, filesystem_id, node_id_to_be_restored):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"nodeIdToBeRestored": node_id_to_be_restored
		}
		commit.add_event({"Filesystem_Restore": sub_payload})