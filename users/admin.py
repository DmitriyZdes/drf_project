from django.contrib import admin

from users.models import Payment


# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('date', 'payed_stage', 'payed_subject', 'sum', 'pay_approach',)
