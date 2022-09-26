# -*- Coding: utf-8 -*-
from typing import Any
import shodan
from settings.config import SHODAN_API_KEY


class ShodanAPI:
    def __init__(self):
        self._api = shodan.Shodan(SHODAN_API_KEY)

    def get_results(self, keyword: str) -> Any:
        return self._api.search(keyword)
