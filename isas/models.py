from django.db import models

class ISA(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField()
    funds = models.ManyToManyField('funds.Fund', through='ISAFund')
    
    def latest_value(self):
        value = 0
        for isafund in self.isafund_set.all():
            value += isafund.quantity * isafund.fund.latest_price()
        return value

    def initial_value(self):
        initial_value = 0
        for isafund in self.isafund_set.all():
            initial_value += isafund.initial_value()
        return initial_value

    def latest_profit(self):
        return self.latest_value() - self.initial_value()

    def latest_profit_per_cent(self):
        return 100.0 * ((self.latest_value() - self.initial_value()) /
                self.initial_value())

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "ISA"
        verbose_name_plural = "ISAs"

class ISAFund(models.Model):
    fund = models.ForeignKey('funds.Fund')
    isa = models.ForeignKey(ISA)
    quantity = models.FloatField()
    price = models.FloatField()

    def initial_value(self):
        return self.quantity * self.price
    
    def latest_value(self):
        return self.quantity * self.fund.latest_price()

    def latest_profit(self):
        return self.latest_value() - self.initial_value()

    def latest_profit_per_cent(self):
        return 100.0 * ((self.latest_value() - self.initial_value()) /
                self.initial_value())

    def __unicode__(self):
        return self.isa.__unicode__() + " - " + self.fund.__unicode__()

