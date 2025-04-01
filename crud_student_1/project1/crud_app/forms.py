from django import forms
from .models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model= Student
        fields='__all__'

        labels={
            's_id':'STUDENT ID',
            'fname':'FIRST NAME',
            'lname':'LAST NAME',
            'div':'DIVISION',
            'mail':'EMAIL ID',
            'marks':'MARKS'
        }