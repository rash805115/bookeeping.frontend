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
		
		try:
			response = self._connection.post_request("filesystem/info", str(payload))
			return True, response["data"]
		except ValueError as error:
			return False, error.args[0]["operation_message"]
	
	def get_all_filesystem(self, user_id):
		user_obj = user.User(self._connection)
		user_node = user_obj.get_user(user_id)[1]["nodeId"]
		
		return xray.Xray(self._connection).xray_node(user_node)
	
	def modify_filesystem(self, nodeid, properties = {}):
		payload = {
			"nodeId": nodeid
		}
		payload.update(properties)
		
		try:
			response = self._connection.post_request("node/modify", str(payload))
			return True, response
		except ValueError as error:
			return False, error.args[0]["operation_message"]
	
	def create_filesystem(self, user_id, filesystem_id, properties = {}):
		payload = {
			"userId": user_id,
			"filesystemId": filesystem_id
		}
		payload.update(properties)
		
		try:
			response = self._connection.post_request("filesystem/create", str(payload))
			return True, response
		except ValueError as error:
			return False, error.args[0]["operation_message"]
	
	def create_filesystem_version(self, commit, node_id, changed_metadata, properties = {}):
		sub_payload = {
			"nodeId": node_id,
			"CHANGE_METADATA": changed_metadata,
		}
		sub_payload.update(properties)
		commit.add_event({"NODE_VERSION": sub_payload})
	
	def delete_filesystem(self, commit, node_id):
		sub_payload = {
			"nodeId": node_id
		}
		commit.add_event({"NODE_DELETE": sub_payload})
	
	def restore_filesystem(self, commit, user_id, filesystem_id, node_id_to_be_restored):
		sub_payload = {
			"userId": user_id,
			"filesystemId": filesystem_id,
			"nodeIdToBeRestored": node_id_to_be_restored
		}
		commit.add_event({"FILESYSTEM_RESTORE": sub_payload})