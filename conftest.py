import pytest
import requests
from selenium import webdriver
from workers.selenium_worker import SeleniumWorker
from workers.playwright_worker import PlaywrightWorker
from src.api.github_api import GitHubAPI
from src.ui.git_hub_app import GitHubApp
from playwright.sync_api import sync_playwright


# API testing
@pytest.fixture
def github_api_worker():
    return GitHubAPI(requests)


# UI testing
@pytest.fixture
def selenium_chrome_worker():
    return SeleniumWorker(webdriver.Chrome())


@pytest.fixture
def git_hub_app_with_selenium_worker_for_chrome(selenium_chrome_worker):
    return GitHubApp(selenium_chrome_worker)


@pytest.fixture
def playwright_chrome_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def playwright_chrome_worker(playwright_chrome_browser):
    return PlaywrightWorker(playwright_chrome_browser)


@pytest.fixture
def git_hub_app_with_playwright_worker_for_chrome(playwright_chrome_worker):
    return GitHubApp(playwright_chrome_worker)
