class TestDynamicControl:

    def test_checkbox_functional(self, dynamic_control):
        dynamic_control.navigate_to('Dynamic Controls')
        dynamic_control.check_text_exist('Dynamic Controls')
        dynamic_control.to_select_checkbox()
        dynamic_control.checkbox_is_check()
        dynamic_control.click_on_button('Remove')
        dynamic_control.wait_loading_not_displayed()
        dynamic_control.check_element_not_exist()
        dynamic_control.check_text_exist("It's gone!")
        dynamic_control.click_on_button('Add')
        dynamic_control.wait_loading_not_displayed()
        dynamic_control.check_element_is_visible('checkbox')

    def test_enable_disable_field(self, dynamic_control):
        dynamic_control.navigate_to('Dynamic Controls')
        dynamic_control.check_element_is_disable()
        dynamic_control.click_on_button('Enable')
        dynamic_control.wait_loading_not_displayed()
        dynamic_control.check_element_is_enable()

