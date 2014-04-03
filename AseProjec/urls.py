import os

from django.conf import settings
from django.conf.urls import patterns, url

from myapp.views import Home, AccountSetting, PostDetail, SignIn, MentorPost, \
	Profile, SignUp, SignOut

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^$', Home.index),
                       url(r'^home$', Home.index),
                       url(r'^index$', Home.index),
                       url(r'^account-setting$', AccountSetting.index),
                        url(r'^blog-single$', PostDetail.index, name='blog-single'),
                        url(r'^mentorpost$', MentorPost.index),
                       url(r'^signin$', SignIn.index, name='signin'),
                       url(r'^profile$', Profile.index, name='profile'),
                       url(r'^signup$', SignUp.index, name='signup'),
                       url(r'^signout$', SignOut.index, name='signout'),
                       url(r'^create-profile$', Profile.createProfile),
                       url(r'^update-profile$', Profile.updateProfile),
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
