from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    # ex : /
    path('', views.index, name='index'),
    # ex ; /signature
    path('date/', views.current_datetime, name='current_datetime'),
    # ex : /book_id
    path("<int:book_id>/", views.detail, name="detail"),
    # ex : /book_id/author
    path("<int:auhtor_id>/author/", views.author, name="author"),
    # ex : /book_id/buy 
    path("<int:book_id>/buy/", views.buy, name="buy"),
]