import os

from pkg_resources import require
from playwright.sync_api import Playwright, expect

import settings


class DownloadFile:

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

    def click_on_button(self, button_name: str):
        self.page.click(f"//button[text()='{button_name}']")

    def navigate_to(self, menu: str):
        self.page.click(f"text={menu}")

    def check_text_exist(self, text: str):
        expect(self.page.locator(f'//*[text()="{text}"]')).to_be_visible()

    def save_file(self, file_name):

        with self.page.expect_download() as download_info:
            self.page.click(f"//*[text() = '{file_name}']")
            download = download_info.value
            file_path = "C:/Users/komishnya.y/PycharmProjects/playwright-educ-test-proj"
            # download.save_as("C:\Users\komishnya.y\PycharmProjects\playwright-educ-test-proj")
            download.save_as(os.path.join(file_path, file_name))

    def check_file_exist_os(self, file_name):

        return os.path.exists(f'C:/Users/komishnya.y/PycharmProjects/playwright-educ-test-proj/{file_name}') is not None
