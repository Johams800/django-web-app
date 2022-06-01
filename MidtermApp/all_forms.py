from django import forms

from .models import Customer, Account, Transaction

class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerModelForm(forms.ModelForm):
    class Meta:
        STATE_CHOICES = [
            ('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'),
            ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'),
            ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'),
            ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
            ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
            ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'),
            ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
            ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'),
            ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'),
            ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
            ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'),
            ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'),
            ('WI', 'Wisconsin'),
            ('WY', 'Wyoming')
        ]
        premium_choice = [('YES', 'Yes'), ('NO', 'No')]

        model = Customer
        exclude = ('premium_choice', )
        labels = '__all__'

        ordering = ['first_name']

        widgets = {
            "state": forms.Select(choices=STATE_CHOICES),
            "preferred_customer": forms.RadioSelect(choices=premium_choice),
            "customer_since": DateInput(),
        }


class AccountModelForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = {'customer'}
        labels = '__all__'

        acc_type = (('Checking', 'Checking'), ('Savings', 'Savings'), ('Investment', 'Investment'))
        text_agree = 'Unless otherwise defined in this Agreement or the context requires otherwise, words and expressions used in this Agreement have the meanings and instructions ascribed to them in the Master Definitions Schedule set out in Schedule 1 of the draft Incorporated Terms Memorandum which will be executed and dated on or about the date of this Agreement and signed for the purpose of identification by the parties to this Agreement and others (as the same may be amended, varied and supplemented from time to time with the consent of the parties to this Agreement, the “Incorporated Terms Memorandum”). This Agreement shall be construed in accordance with the principles of construction and interpretation set out in such Master Definitions Schedule.'
        widgets = {
            "account_type": forms.RadioSelect(choices=acc_type),
            "security_code": forms.PasswordInput(),
        }
    def clean(self):
        balance = self.cleaned_data.get("balance")
        agree = self.cleaned_data.get("agree")

        if balance < 1000:
            self.add_error("", "Minimum of $1000.00 is required for account balance ")

        if agree == False:
            self.add_error("", "Accept terms to proceed!")


class EditAccountModelForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = {'customer', 'balance', 'agreement', 'agree', }
        labels = '__all__'

        acc_type = (('Checking', 'Checking'), ('Savings', 'Savings'), ('Investment', 'Investment'))
        widgets = {
            "balance": forms.IntegerField(disabled=True),
            "account_type": forms.RadioSelect(choices=acc_type)
        }

class TransactionModelForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = {'status', 'account'}
        labels = '__all__'

        trans_type = (('Debit', 'Withdraw'), ('Credit', 'Deposit'))
        widgets = {
            "transaction_type": forms.RadioSelect(choices=trans_type)
        }
    def clean(self):
        amount = self.cleaned_data.get("transaction_amount")
        if amount <= 0:
            self.add_error("", "Transaction amount must be greater than ZERO")
