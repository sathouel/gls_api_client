import base64

import requests as rq

class Client:
    BASE_URL = "https://api.gls-group.eu/public/v1"

    def __init__(self, shipper_id, username, password, language='fr', sandbox=False):
        if language not in ['en', 'fr', 'dk', 'de']:
            raise ValueError("Invalid Language")

        self._shipper_id = shipper_id
        self._username = username
        self._language = language
        self._sandbox = sandbox
        
        self._session = rq.Session()
        self._authenticate(username, password)

        self._resources = {
            "shipments": None,
            "pod": None,
            "tracking": None
        }

    def _authenticate(self, username, password):
        auth = base64.b64encode('{}:{}'.format(username, password).encode()).decode()
        headers = {
            "Accept-Language": self._language,
            "Accept": "application/json",
            "Accept-Encoding": "gzip,deflate",
            "Content-Type": "application/json",
            "Authorization": "Basic {}".format(auth)
        }
        self._session.headers = headers

    @property
    def resources(self):
        pass