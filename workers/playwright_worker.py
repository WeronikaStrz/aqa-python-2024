from typing import Any
from workers.interfaces import WorkerInterface
from playwright.sync_api._generated import Locator, Browser


class PlaywrightWorker(WorkerInterface):
    def __init__(self, browser: Browser) -> None:
        self.page = browser.new_page()

    def go_to_page(self, url: str) -> None:
        self.page.goto(url)

    def find_element_by_id(self, elem_id: str):
        print("here", type(self.page))
        return self.page.locator(f"#{elem_id}")

    def find_element_by_class(self, elem_class: str):
        return self.page.locator(f".{elem_class}")

    def type_text(self, box: Locator, text: str) -> None:
        box.fill(text)

    def click(self, button) -> None:
        button.click()
