from isatracker.isas.models import ISA, ISAFund
from isatracker.funds.models import Fund, FundPrice
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from datetime import date, timedelta
from pygooglechart import Chart, SimpleLineChart, Axis

def index(request):
    isas = ISA.objects.all()
    return render_to_response('isas/index.html', {'isas': isas})

def show(request, isa_id):
    isa = get_object_or_404(ISA, pk=isa_id)
    isafunds = isa.isafund_set.all()
    start_date = isa.created
    end_date = date.today()
    current_date = start_date
    data = []
    while current_date <= end_date:
        value = 0
        for isafund in isafunds:
            try:
                fundprice = isafund.fund.fundprice_set.get(date=current_date)
                value += fundprice.price * isafund.quantity
            except FundPrice.DoesNotExist:
                pass
        data.append(value)
        current_date += timedelta(1)
    chart = SimpleLineChart(500, 200, y_range=[min(data), max(data)])
    chart.add_data(data)
    chart.add_data([data[0], data[0]])
    chart.set_colours(['0000FF', 'AAAAAA'])
    chart.fill_solid('bg', 'DDDDFF')
    chart.set_axis_labels(Axis.LEFT, [int(min(data)), int(max(data))])
    chart.set_axis_labels(Axis.BOTTOM, [start_date, end_date])
    url = chart.get_url()
    return render_to_response('isas/show.html', {'isa': isa, 'chart_url': url})

