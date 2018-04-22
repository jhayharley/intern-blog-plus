from django.contrib.auth import get_user_model
from .forms import RegisterForm
User = get_user_model()
from django.views.generic import (
	ListView,
	DetailView,
	UpdateView,
	CreateView
	)

# Create your views here.

class RegisterView(CreateView):
    form_class               = RegisterForm
    template_name            = 'registration/register.html'
    suuccess                 = '/'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect("/logout")
        return super(RegisterView, self).dispatch(*args, **kwargs)