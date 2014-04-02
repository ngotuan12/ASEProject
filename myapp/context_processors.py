def user(request):
    """A context processor that adds the user to template context"""
    return {
        'user': request.user
    }