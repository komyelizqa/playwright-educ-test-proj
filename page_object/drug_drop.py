from playwright.sync_api import Playwright, expect

import settings


class DrugDrop:

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

    def navigate_to(self, menu: str):
        self.page.click(f"text={menu}")

    def drug_and_drop(self):
        first_element = self.page.locator('#column-a')
        second_element = self.page.locator('id=column-b')
        first_element.drag_to(second_element)

    def check_elements_after_dropping(self):
        expect(self.page.locator('#column-a')).to_have_text('B')
        expect(self.page.locator('id=column-b')).to_have_text('A')

