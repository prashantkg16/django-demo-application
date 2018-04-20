from django.conf.urls import url
from . import views

app_name='devices'
urlpatterns = [
    url(r'^index$', views.index, name='Device home page'),   
    url(r'^addrouter$', views.add_router, name='add '),
    url(r'^editrouter/(?P<id>[0-9]+)$', views.edit_router, name='edit'),
    url(r'^deleterouter/(?P<id>\w+)$', views.delete_router, name='delete'),
    ]
