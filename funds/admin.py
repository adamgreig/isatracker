from isatracker.funds.models import Fund, FidelityFund, FundPrice
from django.contrib import admin

class FundPriceInline(admin.TabularInline):
    model = FundPrice
    extra = 1

class FidelityFundAdmin(admin.ModelAdmin):
    fields = ['name', 'url', 'isin']
    inlines = [FundPriceInline]

admin.site.register(FidelityFund, FidelityFundAdmin)

