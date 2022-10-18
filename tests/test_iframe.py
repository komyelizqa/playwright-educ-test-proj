import settings

class TestIFrames:

    def test_iframes_nested(self, iframe):
        iframe.navigate_to("Frames")
        iframe.check_text_exist("Frames")
        iframe.click_on_button("Nested Frames")
        iframe.navigate_to_frame(settings.IFRAME_LEFT)
