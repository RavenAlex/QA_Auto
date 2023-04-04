import time

from pages.interaction_page import SortablePage


class TestInteractions:

    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_list_order_grid()
            assert list_before != list_after, 'Elements has not been moved'
            assert grid_before != grid_after, 'Elements has not been moved'
