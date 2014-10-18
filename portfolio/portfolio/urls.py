from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^music/', TemplateView.as_view(template_name='music.html')),
    url(r'^code/', TemplateView.as_view(template_name='code.html')),
    url(r'^admin/', include(admin.site.urls)),
)
