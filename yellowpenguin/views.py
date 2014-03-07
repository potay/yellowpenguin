from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from chartit import DataPool, Chart
import transactions.models as transactions
import datetime

# Create your views here.

def index(request):
        latest_transaction_list = transactions.Transaction.objects.order_by('-time_created')[:5]

        context = {
            'latest_transaction_list': latest_transaction_list,
        }
        return render(request, 'index.html', context)

def morrisChartData(request):
        # Chart Data
        start = datetime.datetime.today() - datetime.timedelta(weeks=4)
        end = datetime.datetime.today()
        transObjects = transactions.Transaction.objects.filter(time_created__range=(start, end))
        morris_chart_data = dict()
        morris_chart_data['data'] = []
        for trans in transObjects:
            #morris_chart_data['data'][trans.id] = dict()
            morris_chart_data['data'].append((trans.get_date_isoformat, trans.amount))
        print morris_chart_data
        morris_chart_data['y_label'] = 'Amount'
        morris_chart_data['smooth'] = 'false'

        context = {
            'morris_chart_data': morris_chart_data,
        }
        return render(request, 'js/chart-data-morris.js', context)
