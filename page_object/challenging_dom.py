from playwright.sync_api import Playwright

import settings

from playwright.sync_api import expect


class Dom:

    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()  # self.context.new_page() != Page
        self.base_url = base_url
        self.page.goto(settings.BASE_URL)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

    def check_table_cell(self, name_cell: str):
        table = self.page.locator(f"//*[@id='content']//td[text() = '{name_cell}']")
        expect(table).to_be_visible()

    # expect(table).to_have_text(f'{name_sell}')

    def check_dom_page_opened(self):
        dom_page = self.page.locator('text=Challenging DOM')
        expect(dom_page).to_be_visible()

    def navigate_to(self, menu: str):
        self.page.click(f"text={menu}")

    def button_is_clickable(self):
        first_button = self.page.locator("//div[2]//div[1]/a[1]").all_inner_texts()
        self.page.click('//div[2]//div[1]/a[1]')
        second_button = self.page.locator("//div[2]//div[1]/a[1]").all_inner_texts()
        return first_button != second_button


