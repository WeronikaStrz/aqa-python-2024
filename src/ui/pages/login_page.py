from workers.interfaces import WorkerInterface


class LoginPage:
    URL = "https://github.com/login"
    LOGIN_FLD_ID = "login_field"
    PASSWORD_FLD_ID = "password"
    SIGNIN_BTN_CLASS = "js-sign-in-button"
    BAD_LOGIN_ALERT_CLASS = "js-flash-alert"

    def __init__(self, worker: WorkerInterface):
        self._worker = worker

    def login(self, user: str, password: str):
        self._worker.go_to_page(self.URL)
        username_box = self._worker.find_element_by_id(self.LOGIN_FLD_ID)
        self._worker.type_text(username_box, user)
        password_box = self._worker.find_element_by_id(self.PASSWORD_FLD_ID)
        self._worker.type_text(password_box, password)
        signin_btn = self._worker.find_element_by_class(self.SIGNIN_BTN_CLASS)
        self._worker.click(signin_btn)

    def is_login_succeed(self) -> bool:
        if self._worker.find_element_by_class(self.BAD_LOGIN_ALERT_CLASS):
            return False
        return True
