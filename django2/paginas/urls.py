from django.urls import path
from .views import IndexView ## .views indica que estamos importando do mesmo diretório

urlpatterns = [
    ## path('endereço/', minhaView.as_view(), name='nome da view')
    path('inicio/', IndexView.as_view(), name='inicio'), 
]