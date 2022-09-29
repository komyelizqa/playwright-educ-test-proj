from playwright.sync_api import Playwright

import settings
from page_object.test_cases_page import TestCases


class BaseClass:

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