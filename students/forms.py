from django import forms
from .models import Student
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'status', 'date')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'status': 'Status',
            'date': 'Date and time'
        }

        widgets = {
            'date': DateTimePickerInput()
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "select"



