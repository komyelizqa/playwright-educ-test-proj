from playwright.sync_api import Playwright, expect

import settings


class FormAuth:

    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        # self.page.set_viewport_size({"width": 1800, "height": 1200})
        self.base_url = base_url
        self.page.goto(settings.BASE_URL)

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

    def click_on_button(self, button_name: str):
        self.page.click(f"//*[text()='{button_name}']")

    def check_text_exist(self, text: str):
        expect(self.page.locator(f"//*[text()='{text}']")).to_be_visible()

    def navigate_to(self, menu: str):
        self.page.click(f"text={menu}")

    def login(self, login: str, password: str):
        self.page.fill("//*[@id='username']", login)
        self.page.fill('//*[@id="password"]', password)

    def error_window_is_displayed(self):
        expect(self.page.locator("//*[@id='flash']")).to_be_visible()

    def text_is_displayed(self, expect_text: str):
        actual_text = self.page.locator('//*[@id="flash"]/text()').all_inner_texts()
        return expect_text == actual_text

