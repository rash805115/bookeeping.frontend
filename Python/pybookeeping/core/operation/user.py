class User:
	def __init__(self, connection):
		self._connection = connection
	
	def get_user(self, user_id):
		payload = {
			"userId": user_id
		}
		response = self._connection.request("user/info", payload)
		return response["data"]
	
	def create_user(self, user_id, first_name = None, last_name = None, primary_email = None, secondary_email = None, phone = None):
		payload = {
			"userId": user_id
		}
		if(first_name is not None):
			payload["firstName"] = first_name
		if(last_name is not None):
			payload["lastName"] = last_name
		if(primary_email is not None):
			payload["primaryEmail"] = primary_email
		if(secondary_email is not None):
			payload["secondary_email"] = secondary_email
		if(phone is not None):
			payload["phone"] = phone
			
		return self._connection.request("user/create", payload)