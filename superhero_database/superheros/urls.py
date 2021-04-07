from django.urls import path
from . import views


app_name = 'superheros'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='detail')
]
