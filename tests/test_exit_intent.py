class TestExitIntent:

    def test_window_after_panel(self, desktop_app, entry_ad):
        desktop_app.navigate_to('Exit Intent')
        desktop_app.check_text_exist('Exit Intent')
        desktop_app.move_mouse_up()
        entry_ad.check_text_exist('This is a modal window')
        entry_ad.click_on_button('Close')
        desktop_app.navigate_to('Exit Intent')
