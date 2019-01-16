from django.views import generic
from .models import Subrediti


class SubsView(generic.ListView):
    template_name = 'subrediti.html'
    model = Subrediti
    context_object_name = 'subs'
    ordering = ['created']
    paginate_by = 10


class SubView(generic.DetailView):
    template_name = 'subs/subrediti.html'
    model = Subrediti
