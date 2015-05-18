class User:
	def __init__(self, connection):
		self._connection = connection
	
	def get_user(self, user_id):
		payload = {
			"userId": user_id
		}
		
		try:
			response = self._connection.post_request("user/info", str(payload))
			return True, response["data"]
		except ValueError as error:
			return False, error.args[0]["operation_message"]
	
	def create_user(self, user_id, properties = {}):
		payload = {
			"userId": user_id
		}
		payload.update(properties)
		
		try:
			response = self._connection.post_request("user/create", str(payload))
			return True, response
		except ValueError as error:
			return False, error.args[0]["operation_message"]