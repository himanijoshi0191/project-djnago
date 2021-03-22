
# from django.forms import ModelForm
from django import forms
from add_class.models import StuClassName, StudentInfo

class AddClass(forms.ModelForm):
    class Meta:
        model = StuClassName

        fields = ['class_name']
        

class StudentData(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'

        