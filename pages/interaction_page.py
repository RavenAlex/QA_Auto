import random
import time

from locators.interaction_page_locators import SortablePageLocators, SelectablePageLocators
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