from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import CUSTOMER
from django.db import connection
import json as simplejson
from django.core import serializers

# Create your views here.
def index(request):
    return HttpResponse('<html><head></head><body><h1>I am Ritesh , my first website</h1></body></html>')

def datacount(request):
    template= loader.get_template('transactionbook/second_page.html')
    context ={'namelist1':'ABC',}
    return HttpResponse(template.render(context,request))
    #return ('<html><head></head><body><h1>I am Ritesh , my  2nd Reponse</h1></body></html>')

def summaryresults(request):
    template = loader.get_template('transactionbook/second_page.html')
    cursor = connection.cursor()
    cursor.execute("""SELECT 'Total_Customer_Cnt' AS SUBJECT,COUNT(1) AS cnt FROM CUSTOMER  UNION ALL
                      SELECT 'Total_Customer_Txn_Cnt' AS SUBJECT,COUNT(1) AS cnt FROM CUSTOMER """)
    rows = cursor.fetchall()
    result = {}
    for row in rows:
        result[row[0]] = row[1]
    context = {'namelist1': simplejson.dumps(result)}
    # context =simplejson.dumps(result)
    return HttpResponse(template.render(context, request))
    # return HttpResponse(context['namelist1'])


def datacount1(request):
    template = loader.get_template('transactionbook/second_page.html')
    queryset = CUSTOMER.objects.all()
    data = serializers.serialize('json', queryset)
    #data = list(queryset)  # important: convert the QuerySet to a list object
    #return JsonResponse(data, safe=False)
    context = {'namelist1': simplejson.dumps(data),}
    return HttpResponse(template.render(context, request))
    #return HttpResponse(data)