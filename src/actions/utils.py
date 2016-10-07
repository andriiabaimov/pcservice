# Synonymous with helpers.py

from django.core.exceptions import PermissionDenied


def check_user(request):
    if request.user.is_anonymous():
        raise PermissionDenied
    return request
