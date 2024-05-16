def test_negative_login(GitHubUI):
    # 1. Navigate to login page

    GitHubUI.login_page.navigate_to()

    # 2. Enter wrong creds
    GitHubUI.try_login(username="wrongusername", password="wrongpass")

    # 3.Expected result
    assert GitHubUI.login_page.check_wrong_creds_message()

    # 4. CleanUP
    GitHubUI.close()
