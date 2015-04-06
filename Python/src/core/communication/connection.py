import requests

class Connection():
	def __init__(self, servername, serverport, apiprefix, https = False):
		self._baseurl = ("https" if https else "http") + "://" + servername + ":" + str(serverport) + "/" + apiprefix + "/"
		self._headers = {"Content-Type": "application/json"}
		self.timeout = 10
	
	#This has to be re-worked once issue#9 gets resolved in bookeeping.rest
	def request(self, command, payload):
		response = requests.post(self._baseurl + command, headers = self._headers, data = str(payload), timeout = self.timeout)
		
		if(response.status_code == 200):
			return response.json()
		else:
			return {
				"response": response.status_code,
				"message": "The request was not handled by the server.",
				"url": response.url
			}