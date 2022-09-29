import settings


class TestDynamicLoading:

    def test_hidden_element(self, dynamic_loading):
        dynamic_loading.navigate_to('Dynamic Loading')
        dynamic_loading.check_text_exist(settings.DYNAMIC_LOADING_PAGE)
        dynamic_loading.navigate_to(settings.DYNAMIC_LOADING_FIRST_EXAMPLE)
        dynamic_loading.check_text_exist(settings.DYNAMIC_LOADING_FIRST_EXAMPLE)
        dynamic_loading.check_element_is_hidden()
        dynamic_loading.click_on_button('Start')
        dynamic_loading.wait_loading_not_displayed()
        dynamic_loading.check_text_exist('Hello World!')

    def test_rendering_element(self,dynamic_loading):
        dynamic_loading.navigate_to('Dynamic Loading')
        dynamic_loading.check_text_exist(settings.DYNAMIC_LOADING_PAGE)
        dynamic_loading.navigate_to(settings.DYNAMIC_LOADING_SECOND_EXAMPLE)
        dynamic_loading.check_text_exist(settings.DYNAMIC_LOADING_SECOND_EXAMPLE)
        dynamic_loading.click_on_button('Start')
        dynamic_loading.wait_loading_not_displayed()
        dynamic_loading.check_text_exist('Hello World!')






