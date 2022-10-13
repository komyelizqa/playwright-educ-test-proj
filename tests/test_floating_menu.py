import settings


class TestFloatingMenu:

    def test_menu_is_visible(self, floating_menu):
        floating_menu.navigate_to("Floating Menu")
        floating_menu.check_text_exist("Floating Menu")
        floating_menu.check_button_is_visible("Home")
        floating_menu.check_button_is_visible("News")
        floating_menu.check_button_is_visible("Contact")
        floating_menu.check_button_is_visible("About")

    def test_menu_on_the_top(self, floating_menu):
        floating_menu.navigate_to("Floating Menu")
        floating_menu.click_on_button("Home")
        floating_menu.check_link("home")
        floating_menu.click_on_button("News")
        floating_menu.check_link("news")
        floating_menu.click_on_button("Contact")
        floating_menu.check_link("contact")
        floating_menu.click_on_button("About")
        floating_menu.check_link("about")

    def test_menu_on_the_middle(self, floating_menu):
        floating_menu.navigate_to("Floating Menu")
        floating_menu.scroll_to_text(settings.MIDDLE_PAGE_FLOATING)
        floating_menu.click_on_button("Home")
        floating_menu.check_link("home")
        floating_menu.click_on_button("News")
        floating_menu.check_link("news")
        floating_menu.click_on_button("Contact")
        floating_menu.check_link("contact")
        floating_menu.click_on_button("About")
        floating_menu.check_link("about")

    def test_menu_on_the_down(self, floating_menu):
        floating_menu.navigate_to("Floating Menu")
        floating_menu.scroll_to_element(settings.BUTTON_IN_FOOTER_ES)
        floating_menu.click_on_button("Home")
        floating_menu.check_link("home")
        floating_menu.click_on_button("News")
        floating_menu.check_link("news")
        floating_menu.click_on_button("Contact")
        floating_menu.check_link("contact")
        floating_menu.click_on_button("About")
        floating_menu.check_link("about")





