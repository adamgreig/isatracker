from django.db import models

class ISA(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    funds = models.ManyToManyField('funds.Fund', through='ISAFund')

    def __unicode__(self):
        return self.name

class ISAFund(models.Model):
    fund = models.ForeignKey('funds.Fund')
    isa = models.ForeignKey(ISA)
    quantity = models.FloatField()
    price = models.FloatField()
