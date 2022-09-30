from playwright.sync_api import Playwright, expect

import settings


class DynamicControl:

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

    def to_select_checkbox(self):
        self.page.locator('//*[@id="checkbox"]/input').check()

    def wait_loading_not_displayed(self):
        self.page.wait_for_selector('//*[@id="loading"]', state='hidden')

    def checkbox_is_check(self):
        expect(self.page.locator("//*[@id='checkbox']/input")).to_be_checked()

    def check_element_not_exist(self):
        expect(self.page.locator('//*[@id="checkbox"]/input')).not_to_be_visible()

    def check_element_is_enable(self):
        expect(self.page.locator('//*[@id="input-example"]/input')).to_be_enabled()

    def check_element_is_disable(self):
        expect(self.page.locator('//*[@id="input-example"]/input')).to_be_disabled()

    def check_element_is_visible(self, id_name: str):
        expect(self.page.locator(f'//*[@id="{id_name}"]'))

    def navigate_to(self, menu: str):
        self.page.click(f"text={menu}")