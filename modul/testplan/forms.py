from django.forms import ModelForm, forms
from modul.testplan.models import TestPlan
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, ButtonHolder, Submit, Layout, Div, Fieldset
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab


class PlanNewForm(ModelForm):
    class Meta:
        model = TestPlan
        fields = ['name', 'description', 'tag']

    def __init__(self, *args, **kwargs):
        super(PlanNewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['description'].widget.attrs.update({'class': 'test-descrition-15'})

        self.helper.layout = Layout(
            Field('name'),
            Field('description'),
            Field('tag'),
            ButtonHolder(
                Submit('Save', 'Сохранить', css_class='btn btn-success'),
                Submit('Cansel', 'Отменить', css_class='btn btn-secondary')
            )
        )


class PlanEditForm(ModelForm):
    class Meta:
        model = TestPlan
        fields = ['name', 'description', 'tag']

    def __init__(self, *args, **kwargs):
        super(PlanEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['description'].widget.attrs.update({'class': 'test-descrition-15'})

        self.helper.layout = Layout(
            Field('name'),
            Field('description'),
            Field('tag'),
            ButtonHolder(
                Submit('Save', 'Сохранить', css_class='btn btn-success'),
                Submit('Cansel', 'Отменить', css_class='btn btn-secondary')
            )
        )



