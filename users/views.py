from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic

from users.forms import CookCreationForm


class CookSignUpView(generic.CreateView):
    form_class = CookCreationForm
    template_name = "registration/signup.html"
    # Меняем адрес перенаправления на главную страницу кулинарии
    success_url = reverse_lazy("kitchen:index")

    def form_valid(self, form):
        # Сначала сохраняем пользователя, как это делает стандартный CreateView
        response = super().form_valid(form)
        # Автоматически авторизуем пользователя.
        # self.object — это только что созданный и сохраненный в базу повар.
        login(self.request, self.object)
        return response
