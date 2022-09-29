from playwright.sync_api import Playwright, expect

import settings

class App:

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

    def delete_object_button_by_selector(self):
        row = self.page.query_selector(f'*css=#elements > button')
        row.click()

    def delete_elements_selector_list(self, i: int):
        for i in range(i):
            row = self.page.query_selector(f'*css=#elements > button')
            row.click()

    def navigate_to(self, menu: str):
        self.page.click(f"text={menu}")

    def check_text_exist(self, text: str):
        expect(self.page.locator(f"//*[text()='{text}']")).to_be_visible()

    def login(self, login: str, password: str):
        self.page.fill("some locator", login)
        self.page.fill('some locator', password)

    def create_test(self, test_name: str):
        self.page.fill("ilocator", test_name)

    def add_elements(self):
        self.page.locator("text=Add/Remove Elements").click()
        self.page.locator("//*[text()='Add Element']").click()

    def click_on_list_of_elements(self, i: int, button_name: str):
        for i in range(i):
            self.page.locator(f"text={button_name}").click()

    def check_element_created(self, button_name: str):
        return self.page.locator(f"//*[text()={button_name}") is not None

    def delete_object_button(self, button_name: str):
        self.page.locator(f"//*[text()={button_name}]")

    def check_element_not_exist(self):
        row = self.page.locator('text=Delete')
        expect(row).not_to_be_visible()

    def checkbox_is_uncheck(self, i: int):
        expect(self.page.locator(f"//*[@id='checkboxes']/input[{i}]")).not_to_be_checked()

    def checkbox_is_check(self, i: int):
        expect(self.page.locator(f"//*[@id='checkboxes']/input[{i}]")).to_be_checked()

    def to_select_checkbox(self, i: int):
        self.page.locator(f'//*[@id="checkboxes"]/input[{i}]').check()

    def unselect_checkbox(self, i: int):
        self.page.locator(f'//*[@id="checkboxes"]/input[{i}]').uncheck()

    def check_elements(self):
        list_of_elements = self.page.locator('//*[@id="content"]/div/ul//li').count()
        if list_of_elements == 4:
            self.page.reload()
        else:
            assert list_of_elements == 5
