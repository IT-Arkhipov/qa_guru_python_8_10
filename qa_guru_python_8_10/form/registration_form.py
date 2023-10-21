import os

from selene import browser, have, command, Collection
from selenium.webdriver import Keys


class RegistrationForm:

    def open(self):
        browser.open("/automation-practice-form")

    def fill_user_name(self, first_name: str, last_name: str):
        browser.element('#firstName').type(first_name)
        browser.element('#lastName').type(last_name)

    def fill_email(self, email: str):
        browser.element('#userEmail').type(email)

    def select_gender(self, gender: str):
        browser.element('#genterWrapper').all('label').element_by(have.text(gender)).click()

    def fill_phone(self, number: str):
        browser.element('#userNumber').type(number)

    def fill_birthday(self, date: str):
        browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL + 'a').send_keys(date).press_enter()

    def select_subject(self, subject: str):
        browser.element('#subjectsInput').type(subject).press_enter()

    def select_hobby(self, hobby: str):
        browser.element('#hobbiesWrapper').perform(command.js.scroll_into_view)
        browser.element('#hobbiesWrapper').all('label').element_by(have.text(hobby)).click()

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
