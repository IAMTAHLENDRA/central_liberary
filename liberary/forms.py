from django.contrib.auth.models import User
from django import forms
from .models import Student_Detail



class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class Student_DetailForm(forms.ModelForm):
    class Meta:
        model = Student_Detail
        fields = ('student_name', 'sex', 'branch', 'semester', 'contact_number', )