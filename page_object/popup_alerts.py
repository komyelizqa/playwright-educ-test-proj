
from playwright.sync_api import Playwright, expect

import settings


class PopUpAlerts:

    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.set_viewport_size({"width": 1800, "height": 1200})
        self.base_url = base_url
        self.page.goto(settings.BASE_URL)

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

    def click_on_button(self, button_name: str):
        self.page.click(f"text={button_name}")

    def check_popup_page_is_opened(self):
        text = self.page.locator('//*[@id="content"]//h3')
        expect(text).to_have_text('JavaScript Alerts')

    def check_alert_successfully_closed(self, expect_text: str):
        actual_text = self.page.locator("#result")
        expect(actual_text).to_have_text(expect_text)

    def accept_alert(self):
        self.page.on('dialog', lambda dialog: dialog.accept())
        self.page.evaluate("alert('1')")

    def enter_text_to_prompt(self):
        self.page.on('dialog', lambda dialog: dialog.accept('<3 <3 <3'))

    def handle_prompt_message(self, dialog):
        actual_text = dialog.message
        expect_text = 'I am a JS prompt'
        assert expect_text == actual_text

    def check_alert_message(self, function_for_alert):
        self.page.on('dialog', function_for_alert)

    def handle_alert_message(self, dialog):
        actual_text = dialog.message
        expect_text = 'I am a JS Alert'
        assert expect_text == actual_text

    def handle_confirm_message(self, dialog):
        actual_text = dialog.message
        expect_text = 'I am a JS Confirm'
        assert expect_text == actual_text












