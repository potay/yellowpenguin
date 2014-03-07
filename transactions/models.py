from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.title

class Party(models.Model):
    class Meta:
        verbose_name_plural = "Parties"

    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    phone = models.CharField(max_length=14)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class FinancialAgreement(models.Model):
    INCOME = "In"
    EXPENSES = "Ex"
    TYPE_CHOICES = ( (INCOME, 'Income'), (EXPENSES, 'Expenses'))

    title = models.CharField(max_length=300)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0, verbose_name="Amount")
    users = models.ManyToManyField(User, through="Paymentship")
    party = models.ForeignKey(Party, null=True, blank=True)
    creator = models.ForeignKey(User, verbose_name="Created By", related_name="agreement_creator")
    category = models.ForeignKey(Category)
    time = models.DateTimeField()
    time_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    comments = models.TextField(null=True, blank=True)
    settled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def clean(self):
        if self.settled:
            partyList = dict([(payment.user.username, [0, payment.user]) for payment in Paymentship.objects.filter(agreement=self)])
            for trans in Transaction.objects.filter(agreement=self):
                if trans.to_user:
                    partyList[trans.other_party.username][0] -= trans.amount
                partyList[trans.user.username][0] += trans.amount
            print partyList
            for user in partyList:
                payment = Paymentship.objects.get(agreement=self, user=partyList[user][1])
                print user, int(partyList[user][0]), int(self.amount*payment.weight_numerator/payment.weight_denominator)
                if int(partyList[user][0]) != int(self.amount*payment.weight_numerator/payment.weight_denominator):
                    raise ValidationError(_(u"Agreement is not settled."))



class Transaction(models.Model):
    user = models.ForeignKey(User, verbose_name="User", related_name="transaction_user")
    agreement = models.ForeignKey(FinancialAgreement)
    creator = models.ForeignKey(User, verbose_name="Created By", related_name="transaction_creator")
    to_user = models.BooleanField(default=False)
    other_party = models.ForeignKey(User, related_name="trans_other_party", blank=True, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0, verbose_name="Transaction Amount")
    time = models.DateTimeField()
    time_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    comments = models.TextField(null=True, blank=True)

    def clean(self):
        """
        Validate custom constraints
        """
        if self.amount < 0:
            raise ValidationError(_(u"Not valid transaction amount."))

        if self.to_user and self.other_party is None:
            raise ValidationError(_(u"Thing One is to be used, but it not set!"))

    def title(self):
        return self.user.username+" -> "+self.agreement.title

    def get_to_user(self):
        if self.to_user:
            return self.other_party
        else:
            return "Main Fund"

    get_to_user.short_description = "Paid to?"

    def get_time_created(self):
        return self.time_created.time()

    def get_date_created(self):
        return self.time_created.date()

    def get_time(self):
        return self.time.time()

    def get_date(self):
        return self.time.date()

    def get_between(self, start, end):
        return self.objects.filter(time_created__range=(start, end))

    def get_date_created_isoformat(self):
        return self.get_date_created().isoformat()

    def get_date_isoformat(self):
        return self.get_date().isoformat()

    def get_latest(self, interval=datetime.timedelta(days=7)):
        end = datetime.now()
        start = end - interval
        return self.get_between(self, start, end)

    def __unicode__(self):
        return self.title()

class Paymentship(models.Model):

    user = models.ForeignKey(User)
    agreement = models.ForeignKey(FinancialAgreement)
    weight_numerator = models.IntegerField(max_length=100)
    weight_denominator = models.IntegerField(max_length=100)

    def weight(self):
        return str(self.weight_numerator)+"/"+str(self.weight_denominator)

    weight.default="0"
    weight.blank=True

    def __unicode__(self):
        return self.agreement.title+" <-> "+self.user.username
