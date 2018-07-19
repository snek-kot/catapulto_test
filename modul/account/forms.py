from django.forms import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, ButtonHolder, Submit, Layout
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


# class NewAccountForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         helper = FormHelper()
#         helper.form_method = 'POST'
#
#     def __init__(self, *args, **kwargs):
#         super(NewAccountForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'POST'
#         self.helper.layout = Layout(
#             Field('username'),
#             Field('email'),
#             Field('password'),
#             ButtonHolder(
#                 Submit('Save', 'Сохранить', css_class='btn btn-success'),
#                 Submit('Cansel', 'Отменить', css_class='btn btn-secondary')
#             )
#         )
#
# class PrincipalRegistrationForm(UserCreationForm ):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         helper = FormHelper()
#         helper.form_method = 'POST'
#
#     first_name = forms.CharField(label = 'First name')
#     last_name = forms.CharField(label = 'Last name')
#
#     school = forms.ModelChoiceField(queryset = School.objects.all())
#     profile_pic = forms.FileField(required=False)
#
#
#
#     def save(self,commit = True, uname = "unkown", pword = "unknown"):
#
#         user = super(PrincipalRegistrationForm, self).save(commit = False)
#
#         user.username = uname
#         user.set_password = make_password(pword)
#
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#
#
#         if commit:
#             user.save()
#         return user
#
#     def __init__(self, *args, **kwargs):
#             super(PrincipalRegistrationForm, self).__init__(*args, **kwargs)
#             self.fields.pop('username')
#             self.fields.pop('password1')
#             self.fields.pop('password2')


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


class AuthenticationFormMySelf(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

        # Set the label for the "username" field.
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if self.fields['username'].label is None:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache