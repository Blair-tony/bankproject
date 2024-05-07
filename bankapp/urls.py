from django.urls import path
from .views import *
from .views import AccountListCreateAPIView, AccountDetailAPIView, DepositAPIView, WithdrawalAPIView, TransferAPIView, LoanApplicationListCreateAPIView, LoanApplicationDetailAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('accounts/', AccountListCreateAPIView.as_view(), name='account-list-create'),
    path('accounts/<int:pk>/', AccountDetailAPIView.as_view(), name='account-detail'),
    path('deposit/', DepositAPIView.as_view(), name='deposit'),
    path('withdraw/', WithdrawalAPIView.as_view(), name='withdraw'),
    path('transfer/', TransferAPIView.as_view(), name='transfer'),
    path('loan-applications/', LoanApplicationListCreateAPIView.as_view(), name='loan-application-list-create'),
    path('loan-applications/<int:pk>/', LoanApplicationDetailAPIView.as_view(), name='loan-application-detail'),
]

