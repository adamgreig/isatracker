from isatracker.isas.models import ISA, ISAFund
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from datetime import date
from pygooglechart import Chart, SimpleLineChart, Axis

def index(request):
    isas = ISA.objects.all()
    return render_to_response('isas/index.html', {'isas': isas})

def show(request, isa_id):
    isa = get_object_or_404(ISA, pk=isa_id)
    return render_to_response('isas/show.html', {'isa': isa})

