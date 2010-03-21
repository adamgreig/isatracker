from django.db import models

import urllib2
import BeautifulSoup

class Fund(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField("URL", verify_exists=False)
    def fetch_latest_price(self):
        pass
    def __unicode__(self):
        return self.name

class FundPrice(models.Model):
    fund = models.ForeignKey(Fund)
    date = models.DateField()
    price = models.FloatField()
    def __unicode__(self):
        return self.date.isoformat() + ": " + str(self.price)

class FidelityFund(Fund):
    isin = models.CharField("ISIN", max_length=12)
    def fetch_latest_price(self):
        page = urllib2.urlopen(self.url)
        soup = BeautifulSoup.BeautifulSoup(page)
        return float(soup.find("span", id="buyprice").string)

