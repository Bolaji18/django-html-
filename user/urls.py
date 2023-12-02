from django.urls import path
from . import views


urlpatterns =[
    path('', views.laropad, name='home'),
    path('login/', views.laropad_login, name='login'),
    path('log/', views.user, name='log'),
    path('log/newaccount/', views.new, name='newacc'),
    path('log/rent', views.rent, name='ads'),
    path('log/rent/posted/', views.posted, name='posted'),
    path('newaccount/', views.new, name='newaccount'),
    path('ads/<int:id>', views.advertisement, name='advertisement'),
    path('nonuser/', views.nonusers, name="nonuser"),
]