from django.db import models

# Create your models here.
class Customer(models.Model):
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
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    ssn = models.CharField(max_length=9, null=False)
    customer_since = models.DateField(null=False)
    premium_choice = (('YES', 'Yes'), ('NO', 'No'))
    preferred_customer = models.CharField(max_length=3, choices=premium_choice, default='NO')
    street = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=25, null=False)
    state = models.CharField(max_length=25, choices=STATE_CHOICES)
    zip = models.CharField(max_length=11, null=False)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Account(models.Model):
    text_agree = 'Unless otherwise defined in this Agreement or the context requires otherwise, words and expressions used in this Agreement have the meanings and instructions ascribed to them in the Master Definitions Schedule set out in Schedule 1 of the draft Incorporated Terms Memorandum which will be executed and dated on or about the date of this Agreement and signed for the purpose of identification by the parties to this Agreement and others (as the same may be amended, varied and supplemented from time to time with the consent of the parties to this Agreement, the “Incorporated Terms Memorandum”). This Agreement shall be construed in accordance with the principles of construction and interpretation set out in such Master Definitions Schedule.'
    account_number = models.CharField(max_length=25, null=False)
    acc_type = (('Checking', 'Checking'), ('Savings', 'Savings'), ('Investment', 'Investment'))
    account_type = models.CharField(max_length=15, choices=acc_type, default='Checking')
    balance = models.DecimalField(null=False, default=1000.0, max_digits=12, decimal_places=2)
    security_code = models.CharField(max_length=50, null=False)
    paper_statement = models.BooleanField(default=False, help_text="Check box to receive a paper statement ")
    agreement = models.TextField(default=text_agree)
    agree = models.BooleanField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='account')

    class Meta:
        ordering = ['account_number']

    def __str__(self):
        return self.account_number


class Transaction(models.Model):
    trans_type = (('Debit', 'Withdraw'), ('Credit', 'Deposit'))
    transaction_type = models.CharField(max_length=10, choices=trans_type, null=False, default='Debit')
    transaction_amount = models.DecimalField(max_digits=12, decimal_places=2)
    initiated_date = models.DateTimeField(auto_now=True)
    posted_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, default='Completed')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transaction')

    class Meta:
        ordering = ['initiated_date']

    def __str__(self):
        return self.transaction_amount
