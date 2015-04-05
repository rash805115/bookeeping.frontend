import requests

class BooKeeping_HTTP():
	def __init__(self, servername, serverport, apiprefix, https = False):
		self._baseurl = ("https" if https else "http") + "://" + servername + ":" + str(serverport) + "/" + apiprefix + "/"
		self._headers = {"Content-Type": "application/json"}
	
	def request(self, command, payload):
		response = requests.post(self._baseurl + command, headers = self._headers, data = str(payload))
		return response.json()