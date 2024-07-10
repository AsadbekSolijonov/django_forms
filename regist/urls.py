from django.urls import path
from .views import register_user

urlpatterns = [
    path('', register_user, name='home'),
    # Qo'shimcha yo'nalishlar shu joyda qo'shiladi
]
