from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^archive/$', views.ArichiveView.as_view(), name='archive'),
    url(r'^tags/$', views.TagView.as_view(), name='tags'),
    url(r'^tags/(?P<tag_name>\w+)$', views.TagDetailView.as_view(), name='tag_name'),


]