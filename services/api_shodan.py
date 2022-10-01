# -*- Coding: utf-8 -*-
"""
Module that contains the shodan consumption service.
"""
from typing import Any
import shodan
from settings.config import SHODAN_API_KEY


class ShodanAPI:
    """Component class for the administration of the shodan service."""
    def __init__(self):
        self._api = shodan.Shodan(SHODAN_API_KEY)

    def get_results(self, keyword: str) -> Any:
        """

        Args:
            keyword (str): keyword to search.

        Returns:
             (Any): the search result returned by the shodan api.
        """
        return self._api.search(keyword)
