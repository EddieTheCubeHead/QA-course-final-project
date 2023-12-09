from utils.api_client import PokeApiClient


_LINK_FINDER_REGEX = r""


def _get_urls(raw_json: str) -> list[str]:
    urls = []
    current_word = ""
    inside_quotes = False
    is_url = False
    for character in raw_json:
        if character == "'":
            if inside_quotes:
                if is_url:
                    urls.append(current_word)
                    is_url = False
                elif current_word == "url":
                    is_url = True
                current_word = ""
            inside_quotes = not inside_quotes
            continue
        if inside_quotes:
            current_word += character
    return urls


class LinkWalker:

    def __init__(self, api_client: PokeApiClient):
        self._api_client = api_client

    def assert_links_exist(self, fields: dict):
        raw_json = str(fields)
        urls = _get_urls(raw_json)
        for url in urls:
            print(f"Validating {url}")
            self._api_client.assert_get(url)
