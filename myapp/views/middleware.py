from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from social import exceptions as social_exceptions
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth

class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if hasattr(social_exceptions, 'AuthFailed'):
            print(social_exceptions)
            return HttpResponseRedirect('/error-authenticate')
        else:
            raise exception
class AutoLogout:
    def process_request(self, request):
        if not request.user.is_authenticated() :
            #Can't log out if not logged in
            return
        
        try:
            if datetime.now() - request.session['last_touch'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                auth.logout(request)
                del request.session['last_touch']
                return
        except KeyError:
            pass
        
        request.session['last_touch'] = datetime.now()