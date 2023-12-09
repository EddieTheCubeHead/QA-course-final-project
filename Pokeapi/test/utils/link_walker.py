from utils.api_client import PokeApiClient


class LinkWalker:

    def __init__(self, api_client: PokeApiClient):
        self._api_client = api_client

    def assert_links_exist(self, fields: dict):
        for name, value in fields.items():
            if type(value) is list:
                [self.assert_links_exist(entry) for entry in value]
            elif type(value) is dict:
                self.assert_links_exist(value)
            elif name is "url":
                assert type(value) is str, f"Url '{value}' is not in string format!"
                self._api_client.assert_get(value)
