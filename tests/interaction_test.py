import time

from pages.interaction_page import SortablePage, SelectablePage, ResizablePage


class TestInteractions:

    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_list_order_grid()
            assert list_before != list_after, 'Elements has not been moved'
            assert grid_before != grid_after, 'Elements has not been moved'


    class TestSelectable:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            list_active = selectable_page.click_list()
            grid_active = selectable_page.click_grid()
            assert len(list_active) > 0, 'No elements'
            assert len(grid_active) > 0, 'No elements'


    class TestResizablePage:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_resizable_box()
            max_resize, min_resize = resizable_page.change_resizable()
            assert ('500px', '300px') == max_box, 'Incorrect maximum resize box'
            assert ('150px', '150px') == min_box, 'Incorrect minimum resize box'
            assert min_resize != max_resize, 'Resizable has not been change'

