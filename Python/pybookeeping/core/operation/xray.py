class Xray:
	def __init__(self, connection):
		self._connection = connection
	
	def xray_node(self, node_id):
		payload = {
			"nodeId": node_id
		}
		
		try:
			response = self._connection.post_request("xray/node", str(payload))
			return True, response["data"]
		except ValueError as error:
			return False, error.args[0]["operation_message"]
	
	def xray_full_node(self, node_id):
		payload = {
			"nodeId": node_id
		}
		
		try:
			response = self._connection.post_request("xray/node/full", str(payload))
			return True, response["data"]
		except ValueError as error:
			return False, error.args[0]["operation_message"]
	
	def xray_version(self, node_id):
		payload = {
			"nodeId": node_id
		}
		
		try:
			response = self._connection.post_request("xray/version", str(payload))
			return True, response["data"]
		except ValueError as error:
			return False, error.args[0]["operation_message"]
	
	def xray_deleted(self, node_id):
		payload = {
			"nodeId": node_id
		}
		
		try:
			response = self._connection.post_request("xray/deleted", str(payload))
			return True, response["data"]
		except ValueError as error:
			return False, error.args[0]["operation_message"]
	
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
				is_remote_dir = False
				
				try:
					path = remote_child["directoryPath"]
					name = remote_child["directoryName"]
					is_remote_dir = True
				except KeyError:
					path = remote_child["filePath"]
					name = remote_child["fileName"]
					is_remote_dir = False
			
				key = (path if path == "/" else path + "/") + name
				local_child = self.extract_value(local_xray, key)
				
				if local_child is not None:
					new_entry = self.copy(local_child)
					local_child["visited"] = True
					
					if(local_child["contenthash"] != remote_child["contenthash"]):
						new_entry["change"] = "modify"
					else:
						new_entry["change"] = "none"
					
					new_entry["nodeid"] = remote_child["nodeId"]
					flat_structure[key] = new_entry
				else:
					flat_structure[key] = {
						"directory": is_remote_dir,
						"change": "delete",
						"path": path,
						"name": name,
						"nodeid": remote_child["nodeId"]
					}
				
				children = remote_child["children"] + children
		
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