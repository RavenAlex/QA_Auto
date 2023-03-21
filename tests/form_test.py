import time
from pages.form_page import PracticeFormPage


class TestForm:
    class TestPracticeForm:

        def test_practice_form(self, driver):
            practice_form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
            practice_form_page.open()
            p = practice_form_page.fill_all_fields_and_submit()
            result = practice_form_page.test_practice_form_result()
            assert [p.firstname + ' ' + p.lastname, p.email] == [result[0], result[1]], 'the form has not been filled'

