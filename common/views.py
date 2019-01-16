from django.views import generic


class HomeView(generic.TemplateView):
    """ View da página inicial """
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    