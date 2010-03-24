from isatracker.funds.models import Fund, FundPrice, FidelityFund
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from datetime import date
from pygooglechart import Chart, SimpleLineChart, Axis

def index(request):
    funds = Fund.objects.all()
    return render_to_response('funds/index.html', {'funds': funds})

def show(request, fund_id):
    fund = get_object_or_404(Fund, pk=fund_id)
    prices = fund.fundprice_set.order_by('-date')
    data = []
    for price in prices:
        data.append(price.price)
    data.reverse()
    chart = SimpleLineChart(500, 200, y_range=[min(data), max(data)])
    chart.add_data(data)
    chart.set_colours(['0000FF'])
    chart.fill_solid('bg', 'DDDDFF')
    chart.set_axis_labels(Axis.LEFT, [min(data), max(data)])
    start_date = prices[len(prices) - 1].date.isoformat()
    end_date = prices[0].date.isoformat()
    chart.set_axis_labels(Axis.BOTTOM, [start_date, end_date])
    url = chart.get_url()
    return render_to_response('funds/show.html',
            {'fund': fund, 'prices': prices, 'graph_url': url})

def update_fidelity_prices():
    funds = FidelityFund.objects.all()
    for fund in funds:
        try:
            last_day = fund.fundprice_set.latest('date').date
        except FundPrice.DoesNotExist:
            last_day = date.min

        if last_day != date.today():
            fund.fundprice_set.create(
                    date=date.today(),
                    price=fund.fetch_latest_price())

def update_prices(request):
    update_fidelity_prices()
    return HttpResponse('OK')


