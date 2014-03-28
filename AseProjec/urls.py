from django.conf.urls import patterns, include, url

from myapp import views

from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^$', views.signin),
                       url(r'^home$', views.index),
                       url(r'^index$', views.index),
#                        url(r'^blog-single/(?P<post_id>\d+)$', views.blogSingle, name='detail'),
                        url(r'^blog-single$', views.blogSingle, name='blog-single'),
                       url(r'^signin$', views.signin, name='signin'),
                       url(r'^profile$', views.profile, name='profile'),
                       url(r'^signup$', views.signup, name='signup'),
                       url(r'^people-directory$', views.people),
                       url(regex  = r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], 
    view   = 'django.views.static.serve', 
    kwargs = {'document_root': 'D:/Dev/SourceCode/ASEProject/common',
              'show_indexes' : True})
    # Examples:
    # url(r'^$', 'AseProjec.views.home', name='home'),
    # url(r'^AseProjec/', include('AseProjec.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
