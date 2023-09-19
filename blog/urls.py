from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    #widoki posta
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:poster>/',
         views.post_detail,
         name='post_detail'),
]