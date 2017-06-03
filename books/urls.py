from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^books/add$', views.add),
    url(r'^books/$', views.another),
]