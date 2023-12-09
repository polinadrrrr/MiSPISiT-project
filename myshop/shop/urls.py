from django.urls import include, path
#from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.ProductList, name='ProductList'),
    path('<slug:category_slug>/', views.ProductList, name='ProductListByCategory'),
    path('<int:id>/<slug:slug>/', views.ProductDetail, name='ProductDetail'),
    #url(r'^$', views.ProductList, name='ProductList'),
    #url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    #url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
]