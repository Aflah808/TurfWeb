
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),

    path('booking/',views.book,name='booking'),
    path('slot-book/',views.book_slot,name='book_slot'),
    path('history/', views.history, name='history'),
    
]