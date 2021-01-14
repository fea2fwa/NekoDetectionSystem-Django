from django.views.generic import ListView,DetailView

from api.models import Cat

class CatListView(ListView):
    model = Cat
    context_object_name = 'cat_list'
    template_name = 'cats/cat_list.html'

class CatDetailView(DetailView):
    model = Cat
    context_object_name = 'cat'
    template_name = 'cats/cat_detail.html'
