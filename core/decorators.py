# from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

## Former role access based decorators
# def patient_required(view_func):
#     decorated_view_func = user_passes_test(
#         lambda u: u.is_authenticated and u.role == 'patient'
#     )(view_func)
#     return decorated_view_func

# def staff_required(view_func):
#     decorated_view_func = user_passes_test(
#         lambda u: u.is_authenticated and (u.role == 'staff')
#     )(view_func)
#     return decorated_view_func

def patient_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_patient:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def staff_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view