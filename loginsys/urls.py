from django.conf.urls import include, url
from loginsys.views import login, logout, register


urlpatterns = [
                url(r'^login/', login),
                url(r'^logout/', logout),
                url(r'^register/', register)

]