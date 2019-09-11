from django.conf.urls import url
from django.urls import include
from . import views

urlpatterns = [
    url('^token/$', views.token),
    url('^token/refresh/$', views.refresh_token),
    # url('^sensitive/$', views.sensitive),
    # path('token/revoke/', views.revoke_token),
]
