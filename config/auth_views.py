from django.shortcuts import render
from config.forms import CustomLoginForm, CustomSignupForm


def combined_auth_view(request):
    """Combined login and signup view"""

    # Initialize forms
    login_form = CustomLoginForm()
    signup_form = CustomSignupForm()

    context = {
        'login_form': login_form,
        'signup_form': signup_form,
    }

    return render(request, 'account/auth.html', context)
