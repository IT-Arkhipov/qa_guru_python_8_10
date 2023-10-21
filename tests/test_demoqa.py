import os
from selene import browser, have, command
from selenium.webdriver.common.keys import Keys


def test_demoqa_complete_form():
    # GIVEN
    browser.open("/automation-practice-form")

    # WHEN
    browser.element('#firstName').type('FirstName')
    browser.element('#lastName').type('LastName')

    browser.element('#userEmail').type('mymail@test.ru')
    browser.element('#genterWrapper').all('label').element_by(have.text('Male')).click()
    browser.element('#userNumber').type('9170770905')
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL + 'a').send_keys('11 Oct 2023').press_enter()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('#hobbiesWrapper').perform(command.js.scroll_into_view)
    browser.element('#hobbiesWrapper').all('label').element_by(have.text('Sports')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img/sample.jpg'))
    browser.element('#currentAddress').type('My current address')
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('footer').execute_script('element.remove()')
    browser.element('#submit').perform(command.js.click)

    # THEN
    browser.element('.table-responsive').all('td:nth-of-type(2)').should(have.texts(
        'FirstName LastName',
        'mymail@test.ru',
        'Male',
        '9170770905',
        '11 October,2023',
        'Maths',
        'Sports',
        'sample.jpg',
        'My current address',
        'NCR Delhi'))


# browser.execute_script('document.querySelector("#fixedban").remove()')
