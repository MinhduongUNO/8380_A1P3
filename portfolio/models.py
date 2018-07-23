from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import requests


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    cust_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_number)


class Investment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name='investments')
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    acquired_value = models.FloatField()
    acquired_date = models.DateField(default=timezone.now)
    recent_value = models.FloatField()
    recent_date = models.DateField(default=timezone.now, blank=True, null=True)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer)

    def results_by_investment(self):
        return self.recent_value - self.acquired_value


class Stock(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name='stocks')
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    shares = models.FloatField()
    purchase_price = models.FloatField()
    purchase_date = models.DateField(default=timezone.now, blank=True, null=True)
    #share_value = models.FloatField()
    #purchase_value = models.FloatField()
    #share_price = models.FloatField()

    def created(self):
        self.recent_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer)

    def initial_stock_value(self):
        self.purchase_value = self.shares * self.purchase_price
        return self.purchase_value

    def current_stock_price(self):
        symbol_f = str(self.symbol)
        main_api = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols='
        api_key = '&apikey=JRY009CZ6IW6C5LU'
        url = main_api + symbol_f + api_key
        json_data = requests.get(url).json()
        share = float(json_data["Stock Quotes"][0]["2. price"])
        #self.share_price = share
        return share

    def current_stock_value(self):
        share_value = float(self.current_stock_price()) * float(self.shares)
        return share_value

    def results_by_stocks(self):
        return self.current_stock_value() - self.initial_stock_value()


class Mutual(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name='mutuals')
    mutual = models.CharField(max_length=200)
    initial_value = models.FloatField()
    current_value = models.FloatField()

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer)

    def results_by_mutual(self):
        return self.current_value - self.initial_value