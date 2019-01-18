from django.views import generic
from .models import Subrediti, Thread, Post
from .forms import CreateThreadForm, CreatePostForm
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify


class SubsView(generic.ListView):
    template_name = 'subrediti.html'
    model = Subrediti
    context_object_name = 'subs'
    ordering = ['created']
    paginate_by = 10


class SubView(generic.DetailView):
    template_name = 'subs/subrediti.html'
    model = Subrediti


class CreateSubView(generic.CreateView):
    template_name = 'subs/create_subrediti.html'
    model = Subrediti
    success_url = reverse_lazy('subs:all')
    fields = ['name', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator_id = self.request.user.id  # pega o user logado
        self.object.slug = slugify(self.object.name)
        self.object.save()
        return super(generic.edit.ModelFormMixin, self).form_valid(form)


class CreateThreadView(generic.CreateView):
    template_name = 'subs/create_thread.html'
    model = Thread
    form_class = CreateThreadForm

    def get_initial(self):
        self.subrediti = self.request.GET.get('sub', None)
        return{
            'subrediti': Subrediti.objects.get(id=self.subrediti),
            'author': self.request.user,
        }

    def get_success_url(self):
        subrediti = Subrediti.objects.get(id=self.subrediti)
        return reverse('subs:r', kwargs={'slug': subrediti.slug})


class CreatePostView(generic.CreateView):
    template_name = 'subs/create_post.html'
    model = Post
    form_class = CreatePostForm

    def get_initial(self):
        self.thread = self.request.GET.get('thread', None)

        return{
            'thread': Thread.objects.get(id=self.thread),
            'author': self.request.user,
        }

    def get_success_url(self):
        
        return reverse('subs:all')
