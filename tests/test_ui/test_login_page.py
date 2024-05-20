def test_failed_login_by_playwright(git_hub_app_with_playwright_worker_for_chrome):
    response = git_hub_app_with_playwright_worker_for_chrome.login("Weronika", "4321")
    assert response is False


def test_failed_login_by_selenium(git_hub_app_with_selenium_worker_for_chrome):
    response = git_hub_app_with_selenium_worker_for_chrome.login("Weronika", "4321")
    assert response is False
