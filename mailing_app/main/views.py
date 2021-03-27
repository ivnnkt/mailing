from django.shortcuts import render
from .models import Profile
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Стрница редактирования пользователя.
    """
    model = Profile
    form_class = ProfileForm
    template_name = 'main/profile_edit.html'
    success_url = reverse_lazy('profile', args=[1])

    def test_func(self):
        obj = super(UpdateView, self).get_object()
        return self.request.user.id == obj.pk


class ProfileDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    """Страница отображения данных пользователя (личный кабинет).
    """
    model = Profile
    form_class = ProfileForm
    template_name = 'main/profile.html'

    def test_func(self):
        obj = super(generic.DetailView, self).get_object()
        return self.request.user.id == obj.pk