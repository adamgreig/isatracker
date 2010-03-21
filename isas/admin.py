from isatracker.isas.models import ISA, ISAFund
from django.contrib import admin

class ISAFundInline(admin.TabularInline):
    model = ISAFund
    extra = 1

class ISAAdmin(admin.ModelAdmin):
    inlines = [ISAFundInline]

admin.site.register(ISA, ISAAdmin)
