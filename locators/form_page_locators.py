from selenium.webdriver.common.by import By
import random


class PracticeFormPageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    GENDER_INPUT = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']")
    MOBILE_INPUT = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    SUBJECT_INPUT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    HOBBIES_INPUT = (By.CSS_SELECTOR, f'div[class*="custom-control"] label[for="hobbies-checkbox-{random.randint(1, 3)}"]')
    FILE_INPUT = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    UPLOAD_PICTURE = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS_INPUT = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

#     result
    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
