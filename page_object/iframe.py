from playwright.sync_api import Playwright, expect

import settings


class IFrame:

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

    # noinspection PyTypeChecker
    def navigate_to_frame(self, i_frame_locator: str):
        self.page.wait_for_timeout(1000)
        iframe_locator = self.page.frame(i_frame_locator)
        print(type(iframe_locator))
        expect(self.page.frame(i_frame_locator)).to_be_visible()
        # locator = self.page.frame(i_frame).get_by_text(i_frame_text)
        # expect(locator).to_be_visible()
