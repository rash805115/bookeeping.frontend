class Xray:
	def __init__(self, connection):
		self._connection = connection
	
	def xray_node(self, node_id):
		payload = {
			"nodeId": node_id
		}
		response = self._connection.request("xray/node", payload)
		return response["data"]
	
	def xray_full_node(self, node_id):
		payload = {
			"nodeId": node_id
		}
		response = self._connection.request("xray/node/full", payload)
		return response["data"]
	
	def xray_version(self, node_id):
		payload = {
			"nodeId": node_id
		}
		response = self._connection.request("xray/version", payload)
		return response["data"]
	
	def xray_deleted(self, node_id):
		payload = {
			"nodeId": node_id
		}
		response = self._connection.request("xray/deleted", payload)
		return response["data"]