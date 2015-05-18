import requests

class Connection():
	host = base = None
	https = False
	headers = {}
	port = None
	timeout = 30
	
	def base_url(self):
		if self.port is None:
			return ("https" if self.https else "http") + "://" + self.host + "/" + self.base
		else:
			return ("https" if self.https else "http") + "://" + self.host + ":" + str(self.port) + "/" + self.base
	
	def post_request(self, command, payload):
		response = requests.post(self.base_url() + command, headers = self.headers, data = payload, timeout = self.timeout)
		if(response.status_code >= 200 and response.status_code < 300):
			return response.json()
		else:
			raise ValueError(response.json())
	
	def get_request(self, parameters = []):
		baseurl = self.base_url() + "?"
		for parameter in parameters:
			parameter[0] + "=" + parameter[1] + "&"
		baseurl = baseurl[ : -1]
		
		response = requests.get(baseurl, headers = self.headers, timeout = self.timeout)
		if(response.status_code >= 200 and response.status_code < 300):
			return response.json()
		else:
			raise ValueError(response.json())