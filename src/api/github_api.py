import requests
from requests import Response


class GitHubAPI:
    host = "https://api.github.com/"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    def __init__(self, request_manager: requests) -> None:
        self.request_manager = request_manager

    def get_list_of_repos(self, params: dict) -> Response:
        url = "search/repositories"
        response = self.request_manager.get(
            self.host + url, headers=self.headers, params=params
        )
        return response
