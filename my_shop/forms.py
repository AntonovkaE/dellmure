from django import forms
from django.forms import ModelForm


class SortForm(forms.Form):
    sort_form = forms.TypedChoiceField(label='Сортировать:', choices=[('ПУ', 'По умолчанию'), ('ДТ', 'По дате'), ('ДЕД', 'От дешевых к дорогим'), ('ДОД', 'От дорогих к дешевым')])