from isatracker.funds.models import Fund, FundPrice, FidelityFund
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from datetime import date

def index(request):
    funds = Fund.objects.all()
    return render_to_response('funds/index.html', {'funds': funds})

def show(request, fund_id):
    fund = get_object_or_404(Fund, pk=fund_id)
    return render_to_response('funds/show.html', {'fund': fund})

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


