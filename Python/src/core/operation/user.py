import core.communication.bookeeping_http

class User:
	def __init__(self, servername, serverport, apiprefix, https = False):
		self._server = core.communication.bookeeping_http.BooKeeping_HTTP(servername, serverport, apiprefix, https)
	
	def get_user(self, userid):
		payload = {
			"userId": userid
		}
		return self._server.request("user/info", payload)
	
	def create_user(self, userid, firstname = None, lastname = None, primary_email = None, secondary_email = None, phone = None):
		payload = {
			"userId": userid
		}
		if(firstname is not None):
			payload["firstName"] = firstname
		if(lastname is not None):
			payload["lastName"] = lastname
		if(primary_email is not None):
			payload["primaryEmail"] = primary_email
		if(secondary_email is not None):
			payload["secondary_email"] = secondary_email
		if(phone is not None):
			payload["phone"] = phone
			
		return self._server.request("user/create", payload)