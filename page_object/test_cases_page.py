from playwright.sync_api import Page


class TestCases:
    def __init__(self, page: Page):
        self.page = page

    def delete_object_button_by_selector(self):
        row = self.page.query_selector(f'*css=#elements > button')
        row.click()

    def delete_elements_selector_list(self, i: int):
        for i in range(i):
            row = self.page.query_selector(f'*css=#elements > button')
            row.click()
    ##content > div > button
