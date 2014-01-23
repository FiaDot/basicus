from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'basicus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^board/$', 'board.views.board'),
    url(r'^board/(\d+)/$', 'board.views.article'),
    url(r'^board/write/$', 'board.views.write'),
    url(r'^board/comment/(\d+)/$', 'board.views.comment'),    
)
