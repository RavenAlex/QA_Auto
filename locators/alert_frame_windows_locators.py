from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOWS_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    NEW_TAB_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class AlertsPageLocators:
    CLICK_AND_SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    CLICK_TIMER_SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CLICK_CONFIRM_SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CLICK_PROMT_SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    CONFIRM_TEXT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    INPUT_TEXT = (By.CSS_SELECTOR, 'span[id="promptResult"]')