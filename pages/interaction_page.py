import random
import re
import time

import allure

from locators.interaction_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DraggablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):

    locators = SortablePageLocators()

    @allure.step('Get sortable items')
    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    @allure.step('Change list order')
    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        print(order_before)
        print(order_after)
        return order_before, order_after

    @allure.step('Change list order grid')
    def change_list_order_grid(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):

    locators = SelectablePageLocators()

    @allure.step('Click selectable item')
    def click_selectable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    @allure.step('Change list')
    def click_list(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_items(self.locators.LIST_ITEM)
        active_item = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_item.text

    @allure.step('Change grid')
    def click_grid(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selectable_items(self.locators.GRID_ITEM)
        active_item_grid = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_item_grid.text


class ResizablePage(BasePage):

    locators = ResizablePageLocators()

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    @allure.step('Get max and min size')
    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    @allure.step('Change resizable box')
    def change_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    @allure.step('Change resizable')
    def change_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    @allure.step('Drop simple')
    def drop_simple(self):
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    @allure.step('Drop accept')
    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_div_false = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div_false = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(drag_div_false, drop_div_false)
        text_not_accept = drop_div_false.text
        drag_div = self.element_is_visible(self.locators.ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        text_accept = drop_div.text
        return text_not_accept, text_accept

    @allure.step('Drop prevent')
    def drop_prevent(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        drop_div_inner_not_greedy = self.element_is_visible(self.locators.DROP_HERE_NOT_GREED_INNER)
        drop_div_inner_greedy = self.element_is_visible(self.locators.DROP_HERE_GREED_INNER)
        self.action_drag_and_drop_to_element(drag_div, drop_div_inner_not_greedy)
        outter_not_greed = self.element_is_visible(self.locators.DROP_HERE_NOT_GREED_OUTTER_TEXT).text
        text_not_greed_inner_box = drop_div_inner_not_greedy.text
        self.action_drag_and_drop_to_element(drag_div, drop_div_inner_greedy)
        outter_greed = self.element_is_visible(self.locators.DROP_HERE_GREED).text
        text_greed_inner_box = drop_div_inner_greedy.text
        return outter_not_greed, text_not_greed_inner_box, outter_greed, text_greed_inner_box

    @allure.step('Drop will revert')
    def drop_will_revert(self):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        will_revert = self.element_is_visible(self.locators.WILL_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(will_revert, drop_div)
        position_after_move = will_revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = will_revert.get_attribute('style')
        return position_after_move, position_after_revert

    @allure.step('Drop not revert')
    def drop_not_revert(self):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        not_revert = self.element_is_visible(self.locators.NOT_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(not_revert, drop_div)
        position_after_move = not_revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = not_revert.get_attribute('style')
        return position_after_move, position_after_revert


class DraggablePage(BasePage):
    locators = DraggablePageLocators()

    @allure.step('Simple drag')
    def simple_drag(self):
        self.element_is_visible(self.locators.TAB_SIMPLE).click()
        position_before = self.element_is_visible(self.locators.DRAG_SIMPLE).get_attribute('style')
        drag_me = self.element_is_visible(self.locators.DRAG_SIMPLE)
        self.action_drag_and_drop_by_offset(drag_me, 20, 50)
        position_after = self.element_is_visible(self.locators.DRAG_SIMPLE).get_attribute('style')
        return position_before, position_after

    @allure.step('Get before and after position')
    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0,50), random.randint(0, 50))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    @allure.step('Get top position')
    def get_top_position(self, positions):
        return re.findall('\d[0-9]|\d', positions.split(';')[2])

    @allure.step('Get left position')
    def get_left_positions(self, positions):
        return re.findall('\d[0-9]|\d', positions.split(';')[1])

    @allure.step('Axis drag x')
    def axis_drag_x(self):
        self.element_is_visible(self.locators.TAB_AXIS).click()
        only_x = self.element_is_visible(self.locators.DRAG_X)
        position_x = self.get_before_and_after_position(only_x)
        top_x_before = self.get_top_position(position_x[0])
        top_x_after = self.get_top_position(position_x[1])
        left_x_before = self.get_left_positions(position_x[0])
        left_x_after = self.get_left_positions(position_x[1])
        return [top_x_before, top_x_after], [left_x_before, left_x_after]

    @allure.step('Axis drag y')
    def axis_drag_y(self):
        self.element_is_visible(self.locators.TAB_AXIS).click()
        only_y = self.element_is_visible(self.locators.DRAG_Y)
        position_x = self.get_before_and_after_position(only_y)
        top_y_before = self.get_top_position(position_x[0])
        top_y_after = self.get_top_position(position_x[1])
        left_y_before = self.get_left_positions(position_x[0])
        left_y_after = self.get_left_positions(position_x[1])
        return [top_y_before, top_y_after], [left_y_before, left_y_after]

    @allure.step('Container drag box')
    def container_drag_box(self):
        self.element_is_visible(self.locators.TAB_CONTAINER).click()
        position_box_before = self.element_is_visible(self.locators.DRAG_BOX).get_attribute('style')
        drag_box = self.element_is_visible(self.locators.DRAG_BOX)
        self.action_drag_and_drop_by_offset(drag_box, 1000, 600)
        position_box_after = self.element_is_visible(self.locators.DRAG_BOX).get_attribute('style')
        return position_box_before, position_box_after

    @allure.step('Container drag parent')
    def container_drag_parent(self):
        self.element_is_visible(self.locators.TAB_CONTAINER).click()
        position_parent_before = self.element_is_visible(self.locators.DRAG_PARENT).get_attribute('style')
        drag_parent = self.element_is_visible(self.locators.DRAG_PARENT)
        self.action_drag_and_drop_by_offset(drag_parent, 10, 60)
        position_parent_after = self.element_is_visible(self.locators.DRAG_PARENT).get_attribute('style')
        return position_parent_before, position_parent_after


        # self.element_is_visible(self.locators.TAB_CONTAINER).click()
        # drag_box = self.element_is_visible(self.locators.DRAG_BOX)
        # drag_box_before, drag_box_after = self.get_before_and_after_position(drag_box)
        # return drag_box_before, drag_box_after


