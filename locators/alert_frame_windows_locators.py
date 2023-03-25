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


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    FRAME_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')

class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    TEXT_SMALL_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')
    CLOSE_SMALL_BUTTON = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    TEXT_LARGE_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"] p')
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')
    CLOSE_LARGE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')

