from django.contrib import admin
from .models import CustomUser, Account, Transaction, LoanApplication

admin.site.register(CustomUser)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(LoanApplication)