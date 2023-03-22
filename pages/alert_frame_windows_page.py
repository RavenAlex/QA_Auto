import random
import time

from locators.alert_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_TEXT).text
        return (text_title)


    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOWS_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_TEXT).text
        return (text_title)


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.CLICK_AND_SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return (alert_window.text)

    def check_wait_see_alert(self):
        self.element_is_visible(self.locators.CLICK_TIMER_SEE_ALERT_BUTTON).click()
        time.sleep(6)
        wait_alert_window = self.driver.switch_to.alert
        return (wait_alert_window.text)

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CLICK_CONFIRM_SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_TEXT)
        return (text_result.text)

    def check_input_alert(self):
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.CLICK_PROMT_SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        input_text_result = self.element_is_present(self.locators.INPUT_TEXT)
        return text, input_text_result.text

