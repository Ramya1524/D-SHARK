from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from HRMS.models import Employee


# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ('employee_id', 'name')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Save person'))

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=10)
    password = forms.CharField(label='Password', max_length=8)