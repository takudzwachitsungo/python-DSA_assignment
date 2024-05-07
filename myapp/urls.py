from django.urls import path
from myapp.views import create_record

urlpatterns = [
    path('create/', create_record, name='create_record'),
    # You can add more URL patterns here for other views
]
