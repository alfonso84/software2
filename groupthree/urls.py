"""groupthree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from groupthree.views import Login, Home, SalaPublicaListView, SalaCreateView
from groupthree.datatable import SalaPublicaDatatableView


urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', Login.as_view(), name='login'),
    url(r'^accounts/logout/$', views.logout, {'next_page': '/accounts/login'}, name='logout'),
    url(r'^sala_publica_list/$', SalaPublicaListView.as_view(), name='sala_publica_list'),
    url(r'^sala_publica_data/$', SalaPublicaDatatableView.as_view(), name='sala_publica_data'),
    url(r'^sala_create/$', SalaCreateView.as_view(), name='sala_create'),
]
