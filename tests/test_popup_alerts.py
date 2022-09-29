import settings


class TestPopUpAlerts:

    def test_simple_alert(self, popup_alerts):
        popup_alerts.click_on_button('JavaScript Alerts')
        popup_alerts.check_popup_page_is_opened()
        popup_alerts.accept_alert()
        popup_alerts.check_alert_message(popup_alerts.handle_alert_message)
        popup_alerts.click_on_button('Click for JS Alert')
        popup_alerts.check_alert_successfully_closed(settings.SUCCESS_ALERT)

    def test_dismiss_alert(self, popup_alerts):
        popup_alerts.click_on_button('JavaScript Alerts')
        popup_alerts.click_on_button('Click for JS Confirm')
        popup_alerts.check_alert_successfully_closed(settings.CANCELED_ALERT)

    def test_accept_alert(self, popup_alerts):
        popup_alerts.click_on_button('JavaScript Alerts')
        popup_alerts.accept_alert()
        popup_alerts.check_alert_message(popup_alerts.handle_confirm_message)
        popup_alerts.click_on_button('Click for JS Confirm')
        popup_alerts.check_alert_successfully_closed(settings.ACCEPT_ALERT)

    def test_text_in_prompt(self, popup_alerts):
        popup_alerts.click_on_button('JavaScript Alerts')
        popup_alerts.check_alert_message(popup_alerts.handle_prompt_message)
        popup_alerts.enter_text_to_prompt()
        popup_alerts.click_on_button('Click for JS Prompt')
        popup_alerts.check_alert_successfully_closed('You entered: <3 <3 <3')




