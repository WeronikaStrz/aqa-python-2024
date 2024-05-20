from typing import Any
from workers.interfaces import WorkerInterface
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class SeleniumWorker(WorkerInterface):
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def go_to_page(self, url: str) -> None:
        self.driver.get(url)
        self.driver.implicitly_wait(1)

    def find_element_by_id(self, elem_id: str) -> WebElement:

        element = self.driver.find_element(by=By.ID, value=elem_id)
        return element

    def find_element_by_class(self, elem_class: str) -> WebElement:
        element = self.driver.find_element(by=By.CLASS_NAME, value=elem_class)
        return element

    def type_text(self, box: WebElement, text: str) -> None:
        box.send_keys(text)

    def click(self, button: WebElement) -> None:
        button.click()
