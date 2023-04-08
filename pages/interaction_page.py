import random
import time

from locators.interaction_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DraggablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):

    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

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


    def click_selectable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def click_list(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_items(self.locators.LIST_ITEM)
        active_item = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_item.text

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

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value
    def change_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

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

    def drop_simple(self):
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

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

    def drop_will_revert(self):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        will_revert = self.element_is_visible(self.locators.WILL_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(will_revert, drop_div)
        position_after_move = will_revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = will_revert.get_attribute('style')
        return position_after_move, position_after_revert

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

    def simple_drag(self):
        self.element_is_visible(self.locators.TAB_SIMPLE).click()
        position_before = self.element_is_visible(self.locators.DRAG_SIMPLE).get_attribute('style')
        drag_me = self.element_is_visible(self.locators.DRAG_SIMPLE)
        self.action_drag_and_drop_by_offset(drag_me, 20, 50)
        position_after = self.element_is_visible(self.locators.DRAG_SIMPLE).get_attribute('style')
        return position_before, position_after
