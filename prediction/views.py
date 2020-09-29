from django.shortcuts import render

from .rmt_stockprice import rmt_data

def index(request):
    if request.method == 'POST':
        context = request.POST
        rmt_data(context['stock_id'],context['stock_id2'],context['date'],context['date2'])
        return render(request,'prediction/result.html',context)
    return render(request, 'prediction/index.html')

def result(request):
    return render(request, 'prediction/result.html')
