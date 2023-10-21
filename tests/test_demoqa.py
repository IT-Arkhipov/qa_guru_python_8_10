from selene import have

from qa_guru_python_8_10.form.registration_form import registration_form


def test_demoqa_complete_form():
    # GIVEN
    registration_form.open()

    # WHEN
    registration_form.fill_user_name('FirstName', 'LastName')
    registration_form.fill_email('mymail@test.ru')
    registration_form.select_gender('Male')
    registration_form.fill_phone('9170770905')
    registration_form.fill_birthday('11 Oct 2023')
    registration_form.select_subject('Maths')
    registration_form.select_hobby('Sports')
    registration_form.upload_picture('sample.jpg')
    registration_form.fill_address('My current address')
    registration_form.select_state('NCR')
    registration_form.select_city('Delhi')
    registration_form.submit_form()

    # THEN
    registration_form.registered_info.should(have.exact_texts(
        'FirstName LastName',
        'mymail@test.ru',
        'Male',
        '9170770905',
        '11 October,2023',
        'Maths',
        'Sports',
        'sample.jpg',
        'My current address',
        'NCR Delhi')
    )
