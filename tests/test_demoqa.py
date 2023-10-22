from qa_guru_python_8_10.form.registration_form import RegistrationForm
from qa_guru_python_8_10 import users


def test_demoqa_complete_form():
    registration_form = RegistrationForm()
    # GIVEN
    registration_form.open()

    # WHEN
    registration_form.fill_form(users.user)

    # THEN
    registration_form.assert_registered_info(users.user)