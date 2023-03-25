import random
import time

from locators.alert_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators
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


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frames(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_TEXT).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_TEXT).text
            self.driver.switch_to.default_content()
            return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_modal_dialogs_frame(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        text_small = self.element_is_present(self.locators.TEXT_SMALL_MODAL).text
        self.element_is_visible(self.locators.CLOSE_SMALL_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        text_large = self.element_is_present(self.locators.TEXT_LARGE_MODAL).text
        self.element_is_visible(self.locators.CLOSE_LARGE_BUTTON).click()
        return [title_small, len(text_small)],  [title_large, len(text_large)]



