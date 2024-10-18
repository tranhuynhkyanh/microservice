import os, requests


class AuthService:

    def __init__(self, request):
        self.request = request
        self.data = self.request.get_json()
        self.login_url = os.environ.get('AUTH_SVC_ADDRESS')
        self.register_url = os.environ.get('AUTH_SVC_REGISTER')

    def get_respone(self, response):
        if response.status_code == 200:
            return response.text, None
        else:
            return None, (response.text, response.status_code)

    def login(self):
        auth = self.data

        if not auth:
            return None, ("missing credentials", 401)

        response = requests.post(
            self.login_url, data=auth
        )

        return self.get_respone(response)

    def register(self):
        auth = self.data
        if not auth:
            return None, ("missing credentials", 401)

        response = requests.post(
            self.register_url, data=auth
        )

        return self.get_respone(response)

