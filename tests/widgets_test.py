import time

from thefuzz import fuzz as f

from pages.widgets_page import AccordianPage, AutoCompletePage, DataPickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


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


    class TestSliderAndProgressBar:

        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            value_before, value_after = slider_page.test_slider_change()
            assert value_before != value_after

        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            progress_before, progress_after = progress_bar_page.test_progress_bar()
            assert progress_before != progress_after, 'Progress bar has been not correct work'

    class TestTabs:

        def test_tabs(self, driver):
            test_tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            test_tabs_page.open()
            what_button, what_content = test_tabs_page.test_tabs('what')
            origin_button, origin_content = test_tabs_page.test_tabs('origin')
            use_button, use_content = test_tabs_page.test_tabs('use')
            more_button, more_content = test_tabs_page.test_tabs('more')
            assert what_button == 'What' and what_content != 0, 'The tab "what" is not pressed or text in tab is missing'
            assert origin_button == 'What' and origin_content != 0, 'The tab "origin" is not pressed or text in tab is missing'
            assert use_button == 'What' and use_content != 0, 'The tab "use" is not pressed or text in tab is missing'
            assert more_button == 'What' and more_content != 0, 'The tab "more" is not pressed or text in tab is missing'

    class TestToolTips:

        def test_tool_tips(self, driver):
            test_tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            test_tool_tips_page.open()
            button_text, field_text, contrary_text, section_text = test_tool_tips_page.check_tool_tips()
            assert button_text == 'You hovered over the Button', 'hover missing or incorrect content'
            assert field_text == 'You hovered over the text field', 'hover missing or incorrect content'
            assert contrary_text == 'You hovered over the Contrary', 'hover missing or incorrect content'
            assert section_text == 'You hovered over the 1.10.32', 'hover missing or incorrect content'

    class TestMenu:

        def test_menu(self, driver):
            test_menu_page = MenuPage(driver, 'https://demoqa.com/menu#')
            test_menu_page.open()
            data = test_menu_page.check_menu_items()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3'], "menu items dont exist or have not been selected"



    class TestSelectMenu:

        def test_select_menu(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()
            value, value_input = select_menu_page.field_select_menu()
            f.partial_ratio(value.text, value_input.text)
            select_one_input, name_one = select_menu_page.field_select_one()
            f.partial_ratio(select_one_input.text, name_one)
            select_menu_page.field_old_select()
            select_menu_page.field_multi_select()
            time.sleep(2)




