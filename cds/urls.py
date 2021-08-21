
from django.contrib import admin
from django.urls import path
from cds import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('cds', views.cds, name="cds"),
    path('raashi', views.raashi, name="raashi"),
]
