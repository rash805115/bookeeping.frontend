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
	
	def extract_value(self, local_xray, levels):
		data_dict = local_xray
		for i in levels[:-1]:
			if i in data_dict:
				data_dict = data_dict[i]["children"]
			else:
				return None
		
		try:
			return data_dict[levels[-1]]
		except KeyError:
			return None
	
	def diff(self, local_xray, remote_xray):
		add_list = []
		del_list = []
		modify_list = []
		
		for node in remote_xray:
			children = [node]
			path_list = []
			while len(children) != 0:
				remote_child = children.pop(0)
				
				try:
					path = remote_child["directoryPath"]
					name = remote_child["directoryName"]
				except KeyError:
					path = remote_child["filePath"]
					name = remote_child["fileName"]
			
				key = (path if path == "/" else path + "/") + name
				path_list.append(key)
				local_child = self.extract_value(local_xray, path_list)
				
				if local_child is not None:
					local_child["visited"] = True
					if(local_child["combinedhash"] != remote_child["combinedhash"]):
						modify_list.append([local_child, remote_child])
					
					children = remote_child["children"] + children
				else:
					del_list.append(remote_child)
		
		for key in local_xray:
			children = [key]
			path_list = []
			
			while(len(children) != 0):
				path_list.append(children.pop(0))
				child = self.extract_value(local_xray, path_list)
				
				if "visited" not in child:
					add_list.append(child)
				
				if child["children"] != "none":
					child["path"] = path_list[-1]
					children = list(child["children"].keys()) + children
					
		return add_list, del_list, modify_list