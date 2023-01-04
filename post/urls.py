from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostCreateView.as_view(), name='create'),
    path('greeting/', views.greeting, name='greeting')
]
