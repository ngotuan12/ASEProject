from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from social import exceptions as social_exceptions
from django.http import HttpResponseRedirect

class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if hasattr(social_exceptions, 'AuthFailed'):
            print(social_exceptions)
            return HttpResponseRedirect('/error-authenticate')
        else:
            raise exception
