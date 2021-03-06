from modules.pages.basepage import Basepage
from Locators.locators import CreateAndEditPageLocators

class CreateAndEditPage(Basepage):

    def enter_computer(self, name):
        self.clear_input(*CreateAndEditPageLocators.computer_name_input)
        self.enter_text(name, *CreateAndEditPageLocators.computer_name_input)

    def enter_intro_date(self, date):
        self.clear_input(*CreateAndEditPageLocators.introduced_date)
        self.enter_text(date, *CreateAndEditPageLocators.introduced_date)

    def enter_disc_date(self, date):
        self.clear_input(*CreateAndEditPageLocators.discontinued_date)
        self.enter_text(date, *CreateAndEditPageLocators.discontinued_date)

    def select_company(self, company):
        self.select_dropdown_by_text(company, *CreateAndEditPageLocators.company_dropdown)

    def click_create(self):
        self.click_element(*CreateAndEditPageLocators.create_computer)

    def click_save(self):
        self.click_element(*CreateAndEditPageLocators.update_computer)

    def click_delete_computer(self):
        self.click_element(*CreateAndEditPageLocators.delete_computer_button)

    def click_cancel(self):
        self.click_element(*CreateAndEditPageLocators.cancel_button)

    def isat_createpage(self):
        return self.element_displayed(*CreateAndEditPageLocators.add_computer_title)

    def isat_editpage(self):
        return self.element_displayed(*CreateAndEditPageLocators.add_computer_title)

    def invalid_name_error(self):
        return self.element_displayed(*CreateAndEditPageLocators.computer_name_required)

    def invalid_intro_date_format(self):
        return self.element_displayed(*CreateAndEditPageLocators.invalid_intro_date)

    def invalid_discon_date_format(self):
        return self.element_displayed(*CreateAndEditPageLocators.invalid_dscon_date)

    def get_computer_page_url(self):
        return self.get_page_url()

