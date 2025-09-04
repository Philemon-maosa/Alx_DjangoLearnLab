from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome Admin! You have full control.")
