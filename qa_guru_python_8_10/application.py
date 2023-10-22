from qa_guru_python_8_10.form.left_panel import LeftPanel
from qa_guru_python_8_10.form.registration_form import RegistrationForm


class Application:
    def __init__(self):
        self.simple_registration_form = RegistrationForm()
        self.left_panel = LeftPanel()


app = Application()
