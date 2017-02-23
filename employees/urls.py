from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls), # admin panel
    url(r'^employees?/(.*)', views.api_employee), # api endpoint
]
