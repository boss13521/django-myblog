"""myblog URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from bossblog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('bossblog.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^archive/$', views.ArichiveView.as_view(), name='archive'),
    url(r'^tags/$', views.TagView.as_view(), name='tags'),
    url(r'^tags/(?P<tag_name>\w+)/$', views.TagDetailView.as_view(), name='tag_name'),
    url(r'^blog/(?P<blog_id>\d+)/$', views.BlogDetailView.as_view(), name='blog_id'),


]
