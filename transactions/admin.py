from django.contrib import admin

from transactions.models import Transaction, Category, Paymentship, Party, FinancialAgreement

class CategoryAdmin(admin.ModelAdmin):
    pass

class PartyAdmin(admin.ModelAdmin):
    pass

class PaymentInline(admin.TabularInline):
    model = Paymentship
    extra = 3

class PaymentshipAdmin(admin.ModelAdmin):
    list_display = ('user', 'agreement')
    list_filter = ['user', 'agreement']

class FinancialAgreementAdmin(admin.ModelAdmin):
    inlines = [PaymentInline]

class TransactionAdmin(admin.ModelAdmin):
    #fields = ['user', 'title', 'category', 'inflow', 'outflow']
    """fieldsets = [
        (None,          {'fields': ['cashflow', ]}),
        ('General Information', {'fields': ['title', 'category', 'comments']}),
        ('Parties', {'fields': ['user', 'payee', 'creator']})
    ]"""
    list_display = ('user', 'agreement', 'amount', 'get_to_user', 'time_created')
    list_filter = ['time_created']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'creator':
            kwargs['initial'] = request.user.id
        return super(TransactionAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

admin.site.register(FinancialAgreement, FinancialAgreementAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(Paymentship, PaymentshipAdmin)