class User:
	def __init__(self, connection):
		self._connection = connection
	
	def get_user(self, user_id):
		payload = {
			"userId": user_id
		}
		response = self._connection.request("user/info", payload)
		return response["data"]
	
	def create_user(self, user_id, properties):
		payload = {
			"userId": user_id
		}
		payload.update(properties)
		return self._connection.request("user/create", payload)