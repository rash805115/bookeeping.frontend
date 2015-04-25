class Xray:
	def __init__(self, connection):
		self._connection = connection
	
	def xray_node(self, node_id):
		payload = {
			"nodeId": node_id
		}
		return self._connection.request("xray/node", payload)
	
	def xray_version(self, node_id):
		payload = {
			"nodeId": node_id
		}
		return self._connection.request("xray/version", payload)
	
	def xray_deleted(self, node_id):
		payload = {
			"nodeId": node_id
		}
		return self._connection.request("xray/deleted", payload)