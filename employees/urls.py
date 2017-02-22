from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^employees?/(.*)', views.api_employee),

]

from django.conf.urls import (
        handler400, handler403, handler404, handler500
        )

handler400 = 'my_app.views.bad_request'
