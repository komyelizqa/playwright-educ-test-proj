class TestAddDeleteFeature:

    def test_testcase(self, desktop_app):
        desktop_app.add_elements()
        assert desktop_app.check_element_created('Delete')
        desktop_app.delete_object_button_by_selector()
        desktop_app.check_element_not_exist()

    def test_testcase_another(self, desktop_app):
        desktop_app.navigate_to('Add/Remove Elements')
        desktop_app.click_on_list_of_elements(10, 'Add Element')
        assert desktop_app.check_element_created('Delete')
        desktop_app.delete_elements_selector_list(10)
        desktop_app.check_element_not_exist()

    def test_login(self, desktop_app):
        desktop_app.login("admin", "admin")


