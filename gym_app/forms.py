from django import forms
from .models import Member, Trainer, Class

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone', 'membership_type']

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'specialization', 'experience', 'phone', 'email']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'trainer', 'schedule', 'capacity', 'description']

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Buscar', max_length=100)