class TestPopUpAlerts:

    def test_dropdown(self, dropdown):
        dropdown.click_on_button('Dropdown')
        dropdown.check_text_exist('Dropdown List')
        dropdown.choose_dropdown_by_number()
        dropdown.check_option_selected('Option 2')
        dropdown.choose_dropdown_by_label('Option 1')
        dropdown.check_option_selected('Option 1')
