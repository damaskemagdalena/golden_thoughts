from django.urls import path

from randomthought import views


app_name = 'randomthought'

urlpatterns = [
    path('randomthought/', views.randomthought, name='randomthought')
]