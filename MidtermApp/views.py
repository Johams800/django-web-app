from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView, CreateView

from .all_forms import CustomerModelForm, AccountModelForm, TransactionModelForm, EditAccountModelForm

# Create your views here.
from .models import Customer, Account, Transaction


def details(request):
    customers = Customer.objects.all()
    accounts = Account.objects.all()
    return render(request, 'home.html', {'customers': customers, 'accounts': accounts})


def trans_details(request):
    transactions = Transaction.objects.all()
    accounts = Account.objects.all()
    return render(request, 'transactions.html', {'transactions': transactions, 'accounts': accounts})

class CreateCustomerView(View):
    form_class = CustomerModelForm
    template_name = 'create_customer.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            customer = Customer(first_name=cd['first_name'], last_name=cd['last_name'], ssn=cd['ssn'],
                                customer_since=cd['customer_since'], preferred_customer=cd['preferred_customer'],
                                street=cd['street'], city=cd['city'], state=cd['state'], zip=cd['zip'])
            customer.save()
            return HttpResponseRedirect(reverse(details))
        else:
            return render(request, self.template_name, {'form': form})


class EditCustomerView(UpdateView):
    template_name = 'create_customer.html'
    form_class = CustomerModelForm
    model = Customer
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(reverse(details))

    def get_initial(self, *args, **kwargs):
        initial = super(EditCustomerView, self).get_initial(**kwargs)
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(EditCustomerView, self).get_form_kwargs(*args, **kwargs)
        return kwargs


class AddAccountView(CreateView):
    template_name = 'create_account.html'
    form_class = AccountModelForm
    def form_valid(self, form):
        self.object = form.save(commit=False)
        fk = self.kwargs.get("fk")
        customer = Customer.objects.get(id=fk)
        self.object.customer = customer
        self.object.save()
        return HttpResponseRedirect(reverse(details))

    def get_initial(self, *args, **kwargs):
        initial = super(AddAccountView, self).get_initial(**kwargs)
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(AddAccountView, self).get_form_kwargs(*args, **kwargs)
        return kwargs


class EditAccountView(UpdateView):
    template_name = 'create_account.html'
    form_class = EditAccountModelForm
    model = Account
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(reverse(details))

    def get_initial(self, *args, **kwargs):
        initial = super(EditAccountView, self).get_initial(**kwargs)
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(EditAccountView, self).get_form_kwargs(*args, **kwargs)
        return kwargs


class AddTransaction(CreateView):
    template_name = 'transactions.html'
    form_class = TransactionModelForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        fk = self.kwargs.get("fk")
        account = Account.objects.get(id=fk)
        transact = self.object
        self.object.account = account

        try:
            if transact.transaction_type == 'Credit':
                account.balance = account.balance + transact.transaction_amount
                account.save()
            elif (transact.transaction_type == 'Debit'):
                account.balance = account.balance - transact.transaction_amount
                if account.balance > 1000:
                    account.save()
                else:
                    transact.status = 'Pending'
            else:
                raise ValidationError("All fields are required")
        except:
            form.add_error("", "All fields are required")
        self.object.save()
        return HttpResponseRedirect(reverse(details))

    def get_initial(self, *args, **kwargs):
        initial = super(AddTransaction, self).get_initial(**kwargs)
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(AddTransaction, self).get_form_kwargs(*args, **kwargs)
        return kwargs

    def get(self, request, *args, **kwargs):
        accounts = Account.objects.all()
        fk = self.kwargs.get("fk")
        form = self.form_class()
        transactions = Transaction.objects.filter(account__account_number = Account.objects.get(id=fk))
        paginator = Paginator(transactions, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'accounts': accounts, 'transactions': transactions, 'page_obj': page_obj,
                                                    'form': form})








