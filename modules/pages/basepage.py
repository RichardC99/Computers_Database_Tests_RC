from selenium.webdriver.support.ui import Select

import config

from time import sleep


class Basepage():
    browser = None

    def __init__(self, browser):
        self.browser = browser
        self.base_url = config.url

    def click_element(self, *element):
        self.browser.find_element(*element).click()

    def enter_text(self, text, *element):
        self.browser.find_element(*element).send_keys(text)

    def find_value(self, *element):
       return self.browser.find_element(*element)

    def select_dropdown_by_text(self, value, *element):
        select = Select(self.browser.find_element(*element))
        select.select_by_visible_text(value)

    def clear_input(self, *element):
        self.browser.find_element(*element).clear()

    def element_displayed(self, *element):
        element = self.browser.find_element(*element)

        if element.is_displayed():
            return True
        else:
            return False


    def elements_displayed(self, *element):
        element = self.browser.find_elements(*element)

        if not element:
            return False
        else:
            return True

    def get_page_url(self):
        return self.browser.current_url



