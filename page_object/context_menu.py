
from playwright.sync_api import Playwright, expect

import settings


class ContextMenu:

    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()  # self.context.new_page() != Page
        self.page.set_viewport_size({"width": 1800, "height": 1200})
        self.base_url = base_url
        self.page.goto(settings.BASE_URL)

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

    def right_click(self):
        self.page.locator("//div[@id='hot-spot']").click(button='right')

    def navigate_to(self, menu: str):
        self.page.click(f"text={menu}")

    def check_text_exist(self, text: str):
        expect(self.page.locator(f"//*[text()='{text}']")).to_be_visible()

    def check_context_menu_message(self, function_for_alert):
        self.page.on('dialog', function_for_alert)

    def handle_context_menu_message(self, dialog):
        actual_text = dialog.message
        expect_text = 'You selected a context menu'
        assert expect_text == actual_text

    def accept_alert(self):
        self.page.on('dialog', lambda dialog: dialog.accept())
        self.page.evaluate("alert('1')")

