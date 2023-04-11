import time

import allure

from pages.interaction_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite("Interactions")
class TestInteractions:
    @allure.feature('TestSortable')
    class TestSortablePage:

        @allure.title('Check TestSortable')
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_list_order_grid()
            assert list_before != list_after, 'Elements has not been moved'
            assert grid_before != grid_after, 'Elements has not been moved'

    @allure.feature('TestSelectable')
    class TestSelectable:

        @allure.title('Check Selectable')
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            list_active = selectable_page.click_list()
            grid_active = selectable_page.click_grid()
            assert len(list_active) > 0, 'No elements'
            assert len(grid_active) > 0, 'No elements'

    @allure.feature('TestResizable')
    class TestResizablePage:

        @allure.title('Check Resizable')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_resizable_box()
            max_resize, min_resize = resizable_page.change_resizable()
            assert ('500px', '300px') == max_box, 'Incorrect maximum resize box'
            assert ('150px', '150px') == min_box, 'Incorrect minimum resize box'
            assert min_resize != max_resize, 'Resizable has not been change'

    @allure.feature('TestDroppable')
    class TestDroppablePage:
        @allure.title('Check Droppable')
        def test_drop_simple(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'Simple drop has not been worked'

        @allure.title('Check Drop accept')
        def test_drop_accept(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_not_accept, text_accept = droppable_page.drop_accept()
            assert text_not_accept == 'Drop here', 'Not acceptable drop has not been worked'
            assert text_accept == 'Dropped!', 'Acceptable drop has not been worked'

        @allure.title('Check Drop prevent')
        def test_drop_prevent(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            outter_not_greed, text_not_greed_inner_box, outter_greed, text_greed_inner_box =droppable_page.drop_prevent()
            assert outter_not_greed == text_not_greed_inner_box, 'Not greed drop has not been correct worked'
            assert outter_greed != text_greed_inner_box, 'Greed drop has not been correct worked'

        @allure.title('Check Drop will revert')
        def test_will_revert(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_will_revert()
            assert will_after_move != will_after_revert, 'Will revert has not been worked'

        @allure.title('Check Drop not revert')
        def test_not_revert(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_will_after_move, not_will_after_revert = droppable_page.drop_not_revert()
            assert not_will_after_move == not_will_after_revert, 'Not will revert has not been worked'

    @allure.feature('TestDraggable')
    class TestDraggablePage:

        @allure.title('Check draggable simple')
        def test_draggable_simple(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            position_before, position_after = draggable_page.simple_drag()
            assert position_before != position_after, 'Simple drag and drop has not been worked'

        @allure.title('Check draggable axis')
        def test_draggable_axis(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            top_x, left_x = draggable_page.axis_drag_x()
            top_y, left_y = draggable_page.axis_drag_y()
            assert top_x[0][0] == top_x[1][0] and int(top_x[1][0]) == 0, 'drag-box position has hot been chandged or there has been a shift in the y-axis'
            assert left_x[0][0] != left_x[1][0] and int(left_x[1][0]) != 0, 'drag-box position has hot been chandged or there has been a shift in the y-axis'
            assert top_y[0][0] != top_y[1][0] and int(top_y[1][0]) != 0, 'drag-box position has hot been chandged or there has been a shift in the x-axis'
            assert left_y[0][0] == left_y[1][0] and int(left_y[1][0]) == 0, 'drag-box position has hot been chandged or there has been a shift in the x-axis'

        @allure.title('Check draggable container')
        def test_draggable_container(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            box_before, box_after = draggable_page.container_drag_box()
            parent_before, parent_after = draggable_page.container_drag_parent()
            assert box_before != box_after and box_after == 'position: relative; left: 673px; top: 106px;', \
                'Position box drag has not been changed or was changed on the outside the box'
            assert parent_before != parent_after, 'Position parent drag has not been changed'



