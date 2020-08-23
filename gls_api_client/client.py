import requests as rq

class Client:
    BASE_URL = "https://api.gls-group.eu/public/v1"

    def __init__(self, username, password, sandbox=False):
        self._username = username
        self._sandbox = sandbox
        
        self._authenticate(username, password)

        self._resources = {
            "shipments": None,
            "pod": None,
            "tracking": None
        }

    def _authenticate(self, username, password):
        headers = {

        }
        self._session = rq.Session()
        self._session.headers = headers

    @property
    def resources(self):
        pass