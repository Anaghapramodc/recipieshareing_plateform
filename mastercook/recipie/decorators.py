from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

def custom_login_required(view_func):
    """
    A custom login required decorator that checks if the user is logged in.
    If the user is logged in, it allows access to the view; otherwise, it redirects to the login page.
    """
    decorated_view_func = login_required(view_func)
    return decorated_view_func
