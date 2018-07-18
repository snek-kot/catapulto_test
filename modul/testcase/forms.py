from django.forms import ModelForm, forms
from modul.testcase.models import TestCase
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, ButtonHolder, Submit, Layout, Div, Fieldset
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab


class TestCaseForm(ModelForm):
    class Meta:
        model = TestCase
        fields = ['name', 'precondition', 'description', 'results', ]

    def __init__(self, *args, **kwargs):
        super(TestCaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['results'].widget.attrs.update({'class': 'test-descrition-15'})
        self.helper.layout = Layout(
            Field('name'),
            Field('precondition'),
            Field('description'),
            Field('results'),
            ButtonHolder(
                Submit('Save', 'Сохранить', css_class='btn btn-success'),
                Submit('Cansel', 'Отменить', css_class='btn btn-secondary')
            )

        )
