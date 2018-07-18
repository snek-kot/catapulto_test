from django.forms import ModelForm, forms
from modul.testcase.models import TestCase
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, ButtonHolder, Submit, Layout, Div, Fieldset
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm


class NewAccountForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        helper = FormHelper()
        helper.form_method = 'POST'

    def __init__(self, *args, **kwargs):
        super(NewAccountForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Field('username'),
            Field('email'),
            Field('password'),
            ButtonHolder(
                Submit('Save', 'Сохранить', css_class='btn btn-success'),
                Submit('Cansel', 'Отменить', css_class='btn btn-secondary')
            )
        )


class LoginAccountForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginAccountForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('username'),
            Field('password'),
            ButtonHolder(
                Submit('submit', 'Войти', css_class='btn btn-success')
            )
        )


