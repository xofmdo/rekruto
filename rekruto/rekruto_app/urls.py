from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'rekruto_app'

urlpatterns = [
    path('url_name/', views.index, name='url_name')
]

