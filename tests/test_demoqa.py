from qa_guru_python_8_10.application import app
from qa_guru_python_8_10 import users


def test_demoqa_fill_text_box():
    # GIVEN
    app.left_panel.open_simple_registration_form()

    # WHEN
    app.left_panel.fill_form(users.user)

    # THEN
    app.left_panel.assert_filled_form(users.user)
