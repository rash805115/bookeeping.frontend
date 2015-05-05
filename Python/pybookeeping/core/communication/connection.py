import requests

class Connection():
	def __init__(self, servername = "54.187.230.72", serverport = 8080, apiprefix = "bookeeping.rest/api", https = False):
		self._baseurl = ("https" if https else "http") + "://" + servername + ":" + str(serverport) + "/" + apiprefix + "/"
		self._headers = {"Content-Type": "application/json"}
		self.timeout = 30
	
	def request(self, command, payload):
		response = requests.post(self._baseurl + command, headers = self._headers, data = str(payload), timeout = self.timeout)
		response_dict = response.json()
		
		if(response.status_code >= 200 and response.status_code < 300):
			return response_dict
		else:
			raise ValueError(response_dict["operation_message"] , response_dict)