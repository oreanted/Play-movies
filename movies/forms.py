from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['costumer_name', 'email', 'address', 'city', 'state', 'zip_code', 'card_holder', 'card_number',
                  'Exp_month', 'Exp_year', 'CVV', 'cash']
