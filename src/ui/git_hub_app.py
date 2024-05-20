from workers.interfaces import WorkerInterface
from src.ui.pages.login_page import LoginPage


class GitHubApp:
    def __init__(self, worker: WorkerInterface) -> None:
        self._login_page = LoginPage(worker)

    def login(self, user: str, password: str) -> bool:
        self._login_page.login(user, password)
        return self._login_page.is_login_succeed()
