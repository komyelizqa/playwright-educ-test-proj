import settings


class TestFormAuth:

    def test_form_auth(self, form_auth):
        form_auth.navigate_to("Form Authentication")
        form_auth.check_text_exist("Login Page")
        form_auth.login("hello", "World")
        form_auth.click_on_button(" Login")
        form_auth.error_window_is_displayed()
        form_auth.text_is_displayed(settings.ERROR_AUTH)


