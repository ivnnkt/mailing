from django.shortcuts import render
from .models import Profile
# from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm
from django.urls import reverse_lazy
# from django.http import HttpResponseRedirect

def index(request):
    """Главная страница.
    """

    return render(
        request,
        'main/index.html',
        {
            # 'prod': prod,
        }
    )

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    """Форма редактирования пользователя."""
    model = Profile
    form_class = ProfileForm
    template_name = 'main/profile.html'
    success_url = reverse_lazy('/')