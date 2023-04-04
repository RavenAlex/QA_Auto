from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_FIRST_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECTION_SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_SECOND_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SECTION_THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_THIRD_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-12jo7m5 auto-complete__multi-value__label"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    MULTI_VALUE_REMOVE_ALL = (By.CSS_SELECTOR, 'div[class="auto-complete__indicators css-1wy0on6"]')


class DataPickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEARS = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')


    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


class SliderPageLocators:
    SLIDER_LINE = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarPageLocators:
    STOP_START_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRESS_BAR = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')


class TabsPageLocators:
    WHAT_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    ORIGIN_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    USE_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    MORE_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')
    WHAT_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    ORIGIN_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    USE_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')
    MORE_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]')


class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')
    FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    TOOL_TIP_FIELD = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')
    CONTRARY_LINK = (By.XPATH, '//*[.="Contrary"]')
    TOOL_TIP_CONTRARY = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')
    SECTION_LINK = (By.XPATH, '//*[.="1.10.32"]')
    TOOL_TIP_SECTION = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')
    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')

class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')


class SelectMenuPageLocators:
    VALUE = (By.CSS_SELECTOR, 'div[id="withOptGroup"]')
    VALUE_FIELD = (By.CSS_SELECTOR, 'input[id="react-select-2-input"]')
    SELECT_ONE = (By.CSS_SELECTOR, 'div[id="selectOne"]')
    SELECT_ONE_FIELD = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    OLD_STYLE_SELECT = (By.CSS_SELECTOR, 'select[id="oldSelectMenu"]')
    MULTI_SELECT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')













