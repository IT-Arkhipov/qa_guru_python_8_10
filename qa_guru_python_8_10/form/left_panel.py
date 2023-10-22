from selene import browser, have, query

from qa_guru_python_8_10.users import User


class LeftPanel:

    def __init__(self):
        self.full_name = browser.element('#userName')
        self.user_email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.output = browser.element('#output')
        self.output_name = self.output.element('#name')
        self.output_email = self.output.element('#email')
        self.output_current_address = self.output.element('#currentAddress')
        self.output_permanent_address = self.output.element('#permanentAddress')

        self.open_simple_registration_form = self.open


    def open(self):
        browser.open('/text-box')


    def fill_form(self, user: User):
        self.full_name.type(user.full_name)
        self.user_email.type(user.email)
        self.current_address.type(user.current_address)
        self.permanent_address.type(user.permanent_address)
        browser.element('#submit').press_enter()


    def assert_filled_form(self, user: User):
        self.output_name.should(have.exact_text(f'Name:{user.full_name}'))
        self.output_email.should(have.exact_text(f'Email:{user.email}'))
        self.output_current_address.should(have.exact_text(f'Current Address :{user.current_address}'))
        self.output_permanent_address.should(have.exact_text(f'Permananet Address :{user.permanent_address}'))