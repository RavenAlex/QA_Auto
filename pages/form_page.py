import os

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import PracticeFormPageLocators
from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    locators = PracticeFormPageLocators()

    def fill_all_fields_and_submit(self):
        person_info_pf = next(generated_person())
        file_name, path = generated_file()
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person_info_pf.firstname)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person_info_pf.lastname)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person_info_pf.email)
        self.element_is_visible(self.locators.GENDER_INPUT).click()
        self.element_is_visible(self.locators.MOBILE_INPUT).send_keys(person_info_pf.mobile)
        self.element_is_visible(self.locators.SUBJECT_INPUT).send_keys('Maths')
        self.element_is_visible(self.locators.SUBJECT_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES_INPUT).click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_INPUT).send_keys(person_info_pf.current_address)
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return person_info_pf

    def test_practice_form_result(self):
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            data.append(item.text)
        return data




