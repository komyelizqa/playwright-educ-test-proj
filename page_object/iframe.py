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

    def check_frame(self, i_frame_locator: str, iframe_text: str):
        self.page.wait_for_timeout(1000)
        iframe_locator = self.page.frame(i_frame_locator)

        body = iframe_locator.wait_for_selector("body")
        visible = body.is_visible()
        text = body.inner_text()

        assert visible and iframe_text in text

    def check_frame_field(self):
        self.page.wait_for_timeout(1000)
        iframe_text = 'Your content goes here.'
        iframe_locator = self.page.frame('mce_0_ifr')

        iframe_field = iframe_locator.wait_for_selector("p")
        visible = iframe_field.is_visible()
        text = iframe_field.inner_text()

        assert visible and iframe_text in text

    def clear_field(self):
        self.page.keyboard.press('Backspace')

    def input_frame_field(self):
        self.page.wait_for_timeout(1000)
        iframe_text = 'London is a capital of GrateBritain'
        iframe_locator = self.page.frame('mce_0_ifr')

        iframe_field = iframe_locator.wait_for_selector("p")
        iframe_field.fill(iframe_text)
        text = iframe_field.inner_text()
        assert iframe_text in text
