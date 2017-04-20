from django.conf.urls import include, url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
                    url(r'^connection/$', TemplateView.as_view(template_name='login.html')),
                    url(r'^$', views.products, name='products'),
                    url(r'^sort/phone/$', views.sort_phone, name='sort_phone'),
                    url(r'^sort/tablets/$', views.tablets, name='tablets'),
                    url(r'^sort/smartphone/$', views.smartphone, name='smartphone'),
                    url(r'^products/(?P<product_id>\d+)/$', views.product, name='product'),
                    url(r'^cart/$', views.cart, name='cart'),
]