import time

from pages.alert_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage


class TestAlertFrameWindows:
    class TestBrowserWindows:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', 'New tab has not been opened or an incorrect tab has opened'

        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            text_result = new_window_page.check_opened_new_window()
            assert text_result == 'This is a sample page', 'New window has not been opened or an incorrect window has ' \
                                                           'opened'

    class TestAlerts:

        def test_see_alert(self, driver):
            alert_test = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_test.open()
            see_alert_text = alert_test.check_see_alert()
            assert see_alert_text == 'You clicked a button', 'Click button has not been worked or an incorrect text ' \
                                                             'in alert '

        def test_five_sec_alert(self, driver):
            wait_alert_test = AlertsPage(driver, 'https://demoqa.com/alerts')
            wait_alert_test.open()
            wait_test_result = wait_alert_test.check_wait_see_alert()
            assert wait_test_result == 'This alert appeared after 5 seconds', 'Click button has not been worked or an ' \
                                                                              'incorrect text in alert '

        def test_click_alert(self, driver):
            click_alert_test = AlertsPage(driver, 'https://demoqa.com/alerts')
            click_alert_test.open()
            click_alert_test_result = click_alert_test.check_confirm_alert()
            assert click_alert_test_result == 'You selected Ok', 'Click button has not been worked or an incorrect ' \
                                                                 'text in alert '

        def test_input_alert(self, driver):
            click_input_alert_test = AlertsPage(driver, 'https://demoqa.com/alerts')
            click_input_alert_test.open()
            text, alert_text = click_input_alert_test.check_input_alert()
            assert alert_text == f'You entered {text}', 'Click button has not been worked or an incorrect text in alert'

    class TestFrames:

        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            result_frame1 = frames_page.check_frames('frame1')
            result_frame2 = frames_page.check_frames('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'First frame does not exist'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'Second frame does not exist'
