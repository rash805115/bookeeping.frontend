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
	
	def generate_path(self, path):
		pieces = path.split("/")
		levels = []
		
		for i in range(2, len(pieces) + 1):
			shard = pieces[0 : i]
			levels.append("/".join(shard))
		
		return levels
	
	def extract_value(self, local_xray, path):
		levels = self.generate_path(path)
		data_dict = local_xray
		for i in levels[ : -1]:
			if i in data_dict:
				data_dict = data_dict[i]["children"]
			else:
				return None
		
		try:
			return data_dict[levels[-1]]
		except KeyError:
			return None
	
	def copy(self, src_dict):
		copy_dict = {}
		for key in src_dict:
			if not isinstance(src_dict[key], dict):
				copy_dict[key] = src_dict[key]
		
		return copy_dict
	
	def diff(self, local_xray, remote_xray):
		flat_structure = {}
		for node in remote_xray:
			children = [node]
			while len(children) != 0:
				remote_child = children.pop(0)
				
				try:
					path = remote_child["directoryPath"]
					name = remote_child["directoryName"]
				except KeyError:
					path = remote_child["filePath"]
					name = remote_child["fileName"]
			
				key = (path if path == "/" else path + "/") + name
				local_child = self.extract_value(local_xray, key)
				
				if local_child is not None:
					new_entry = self.copy(local_child)
					local_child["visited"] = True
					
					if(local_child["contenthash"] != remote_child["contenthash"]):
						new_entry["change"] = "modify"
					else:
						new_entry["change"] = "none"
					
					flat_structure[key] = new_entry
					children = remote_child["children"] + children
				else:
					flat_structure[key] = {"change": "delete"}
		
		for key in local_xray:
			children = [key]
			
			while(len(children) != 0):
				child_path = children.pop(0)
				child = self.extract_value(local_xray, child_path)
				
				if "visited" not in child:
					new_entry = self.copy(child)
					new_entry["change"] = "add"
					flat_structure[child_path] = new_entry
				
				if child["children"] != "none":
					children = list(child["children"].keys()) + children
					
		return flat_structure