import requests
from requests.auth import HTTPBasicAuth

class api(object):

    class DataUnavailable(Exception):
        """Catch-all exception indicating we can't get data back from the API"""

    def __init__(self, api_key):
        self._apiKey =api_key
        self._baseURL = "https://api.octopus.energy/v1"
        self._productCode = ""
        self._tariffCode = ""
        self._gsp = ""
        self.session = requests.Session()

    def _get(self, path, params=None):
        """Make a GET HTTP request"""
        if params is None:
            params = {}
        url = self._baseURL + path
        try:
            response = self.session.request(method="GET", auth=(self._apiKey,''), url=url, params=params)
        except requests.RequestException as e:
            raise self.DataUnavailable("Network exception") from e

        if response.status_code != 200:
            raise self.DataUnavailable("Unexpected response status (%s)" % response.status_code)

        return response.json()

