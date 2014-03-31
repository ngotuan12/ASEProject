import os

from django.conf import settings
from django.conf.urls import patterns, include, url

from myapp import views


dirx = str(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
print(os.pardir+'/common')
print(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))+"/common")
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^$', views.signin),
                       url(r'^home$', views.index),
                       url(r'^index$', views.index),
                       url(r'^account-setting$', views.accountSetting),
                        url(r'^blog-single$', views.blogSingle, name='blog-single'),
                        url(r'^mentorpost$', views.mentorpost),
                       url(r'^signin$', views.signin, name='signin'),
                       url(r'^profile$', views.profile, name='profile'),
                       url(r'^signup$', views.signup, name='signup'),
                       url(r'^people-directory$', views.people),
                       url(r'^create-profile$', views.createProfile),
                       url(r'^update-profile$', views.updateProfile),
                       url(regex  = r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], 
    view   = 'django.views.static.serve', 
    kwargs = {'document_root': os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))+"/common",
              'show_indexes' : True})
    # Examples:
    # url(r'^$', 'AseProjec.views.home', name='home'),
    # url(r'^AseProjec/', include('AseProjec.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
