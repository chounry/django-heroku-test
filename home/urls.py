from django.conf.urls import url
from . import views

app = 'home'

urlpatterns = [
    url(r'^$',views.home, name = 'home-page')
]