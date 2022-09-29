from playwright.sync_api import Playwright, expect

import settings


class Dropdown:

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

    def check_text_exist(self, text: str):
        expect(self.page.locator(f"//*[text()='{text}']")).to_be_visible()

    def choose_dropdown_by_number(self):
        self.page.locator('//*[@id = "dropdown"]').select_option(index=2)

    def choose_dropdown_by_label(self, name_string: str):
        self.page.locator('//*[@id = "dropdown"]').select_option(label=f'{name_string}')

    def check_option_selected(self, option: str):
        self.page.is_visible(f"//*[@selected='{option}']")
        self.page.wait_for_timeout(1000)




