from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict

# Create your views here.
from transactions.models import *

def index(request):
    latest_transaction_list = Transaction.objects.order_by('-time_created')[:5]
    context = {
        'latest_transaction_list': latest_transaction_list,
    }
    return render(request, 'transactions/index.html', context)

def detail(request, trans_id):
    transaction = get_object_or_404(Transaction, id=trans_id)
    details = model_to_dict(transaction)
    print details
    return render(request, 'transactions/detail.html', {'transaction': transaction, 'details': details})

def add(request):
    return render(request, 'transactions/detail.html', {})

def edit(request, trans_id):
    transaction = get_object_or_404(Transaction, id=trans_id)
    return render(request, 'transactions/detail.html', {'transaction': transaction})