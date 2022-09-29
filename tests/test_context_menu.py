class TestContextMenu:

    def test_context_menu(self, context_menu_page):
        context_menu_page.navigate_to('Context Menu')
        context_menu_page.check_text_exist('Context Menu')
        context_menu_page.accept_alert()
        context_menu_page.check_context_menu_message(context_menu_page.handle_context_menu_message)
        context_menu_page.right_click()
