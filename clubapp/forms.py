from django.forms import ModelForm
from .models import مطلب_حجز_قاعة,بيانات_النادي,مطلب_نشاط,مطلب_نشاط
from django import forms
class DemandeDeSalleForm(ModelForm,forms.Form):
    class Meta :
        model = مطلب_حجز_قاعة
        fields = "__all__"
    تحديد_اليوم_و_التوقيت = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )
class DemandeEvenementForm(ModelForm,forms.Form):
    class Meta :
        model = مطلب_نشاط
        fields = "__all__"
    الزمان =  forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )