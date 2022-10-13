from playwright.sync_api import Playwright, expect

import settings


class FloatingMenu:
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

    def check_link(self, menu_name: str):
        expect(self.page).to_have_url(f"https://the-internet.herokuapp.com/floating_menu#{menu_name}")

    def scroll_to_element(self, text: str):
        self.page.locator(text).scroll_into_view_if_needed()
        expect(self.page.locator(text)).to_be_visible()

    def check_button_is_visible(self, button_name: str):
        button = self.page.locator(f"//*[text()='{button_name}']")
        expect(button).to_be_visible()

