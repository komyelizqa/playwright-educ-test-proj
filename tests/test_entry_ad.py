class TestEntryAd:

    def test_close_ad(self, entry_ad):
        entry_ad.navigate_to('Entry Ad')
        entry_ad.check_text_exist('This is a modal window')
        entry_ad.click_on_button('Close')
        entry_ad.check_text_exist('Entry Ad')
