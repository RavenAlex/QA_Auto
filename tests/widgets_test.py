import time
from pages.widgets_page import AccordianPage, AutoCompletePage, DataPickerPage


class TestWidgets:

    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'


    class TestAutoComplete:

        def test_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multi()
            colors_result = auto_complete_page.check_color_in_multi()
            print(colors)
            print(colors_result)
            assert colors == colors_result, 'TThe added colors are missing in the input'

        def test_remove_value_from_multi(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
            print(count_value_before)
            print(count_value_after)
            assert count_value_before != count_value_after, 'Value was not deleted'

        def test_fill_single_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_input_single()
            color_result = auto_complete_page.check_color_in_single()
            assert color == color_result, 'The added color is missing in the input'


        def test_remove_all(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            time.sleep(1)
            auto_complete_page.check_remove_all_color()
            time.sleep(2)


    class TestDatePickerPage:

        def test_change_data(self, driver):
            data_picker_page = DataPickerPage(driver, 'https://demoqa.com/date-picker')
            data_picker_page.open()
            value_date_before, value_date_after = data_picker_page.select_date()
            assert value_date_before != value_date_after


        def test_change_data_and_time(self, driver):
            data_picker_page = DataPickerPage(driver, 'https://demoqa.com/date-picker')
            data_picker_page.open()
            value_date_before, value_date_after = data_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after




