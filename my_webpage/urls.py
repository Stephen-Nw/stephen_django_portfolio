from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('portfolio/<slug:slug>', views.portfolio_item, name='portfolio-info')
]
