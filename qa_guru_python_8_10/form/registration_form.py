import os
from enum import Enum
from selene import browser, have, command
from selenium.webdriver import Keys


class RegistrationForm:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.gender = browser.element('#genterWrapper')
        self.phone_number = browser.element('#userNumber')
        self.birth_day = browser.element('#dateOfBirthInput')
        self.subject = browser.element('#subjectsInput')
        self.hobby = browser.element('#hobbiesWrapper')

    def open(self):
        browser.open("/automation-practice-form")

    def fill_user_name(self, first_name: str, last_name: str):
        self.first_name.type(first_name)
        self.last_name.type(last_name)

    def fill_email(self, email: str):
        self.user_email.type(email)

    def select_gender(self, gender: Enum):
        self.gender.all('label').element_by(have.text(gender)).click()

    def fill_phone(self, number: str):
        self.phone_number.type(number)

    def fill_birthday(self, date: str):
        self.birth_day.send_keys(Keys.CONTROL + 'a').send_keys(date).press_enter()

    def select_subject(self, subject: str):
        self.subject.type(subject).press_enter()

    def select_hobby(self, hobby: Enum):
        self.hobby.perform(command.js.scroll_into_view)
        self.hobby.all('label').element_by(have.text(hobby)).click()

    def upload_picture(self, file_name: str):
        browser.element('#uploadPicture').send_keys(os.path.abspath('img/' + file_name))

    def fill_address(self, address: str):
        browser.element('#currentAddress').type(address)

    def select_state(self, state: str):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.element('#react-select-3-input').type(state).press_enter()

    def select_city(self, city: str):
        browser.element('#city').click()
        browser.element('#react-select-4-input').type(city).press_enter()

    def submit_form(self):
        browser.element('footer').execute_script('element.remove()')
        browser.element('#submit').perform(command.js.click)

    def assert_registered_info(self, *args):
        browser.element('.table-responsive').all('td:nth-of-type(2)').should(have.exact_texts(args))
