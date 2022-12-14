from playwright.sync_api import Playwright, expect

import settings


class DynamicLoading:

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
        self.page.click(f"//button[text()='{button_name}']")

    def check_text_exist(self, text: str):
        expect(self.page.locator(f'//*[text()="{text}"]')).to_be_visible()

    def navigate_to(self, menu: str):
        self.page.click(f"text={menu}")

    def check_element_is_hidden(self):
        expect(self.page.locator('//*[text() = "Hello World!"]')).to_be_hidden()

    def wait_loading_not_displayed(self):
        self.page.wait_for_selector('//*[@id="loading"]', state='hidden')
