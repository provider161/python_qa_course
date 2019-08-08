"""
Fixture for HTTP requests to specific API
"""

import requests


class APIClient:
    """
    Упрощенный клиент для работы с API
    Инициализируется базовым url на который пойдут запросы
    """
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, params=None, data=None, headers=None):
        return requests.post(url=self.base_url, params=params, data=data, headers=headers)

    def get(self, params=None):
        return requests.get(url=self.base_url, params=params)
