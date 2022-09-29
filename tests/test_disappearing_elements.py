class TestDisappearingElements:

    def test_elements_exist(self, desktop_app):
        desktop_app.navigate_to("Disappearing Elements")
        desktop_app.check_text_exist('Disappearing Elements')
        desktop_app.check_elements()
