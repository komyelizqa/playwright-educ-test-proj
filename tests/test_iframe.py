import settings


class TestIFrames:

    def test_frames_nested(self, iframe):
        iframe.navigate_to("Frames")
        iframe.check_text_exist("Frames")
        iframe.click_on_button("Nested Frames")
        iframe.check_frame(settings.IFRAME_LEFT, "LEFT")
        iframe.check_frame(settings.IFRAME_MIDDLE, "MIDDLE")
        iframe.check_frame(settings.IFRAME_RIGHT, "RIGHT")
        iframe.check_frame(settings.IFRAME_BOTTOM, "BOTTOM")

    def test_iframe(self, iframe):
        iframe.navigate_to("Frames")
        iframe.check_text_exist("Frames")
        iframe.click_on_button("iFrame")
        iframe.check_text_exist(settings.IFRAME_TEXT)
