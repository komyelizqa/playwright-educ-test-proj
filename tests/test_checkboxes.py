class TestCheckboxes:

    def test_checkboxes(self, desktop_app):
        desktop_app.navigate_to("Checkboxes")
        desktop_app.check_text_exist('Checkboxes')
        desktop_app.to_select_checkbox(1)
        desktop_app.checkbox_is_check(2)
        desktop_app.to_select_checkbox(1)
        desktop_app.checkbox_is_check(1)
        desktop_app.unselect_checkbox(1)
        desktop_app.unselect_checkbox(2)
        desktop_app.checkbox_is_uncheck(1)
        desktop_app.checkbox_is_uncheck(2)





