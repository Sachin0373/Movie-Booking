from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView,TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Person


# Create your views here.
@login_required
def myview(request):
    return render(request,'app/my_view.html')

class home_page(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'app/signup.html'


class Thankyouview(TemplateView):
    template_name = 'app/thankyou.html'


def design_page(request):
    return render(request,'app/home.html')

class PersonCreateView(CreateView):
    model = Person
    fields ='__all__'
    success_url = reverse_lazy('app:thankyou')


class PersonListView(ListView):
    model = Person
    queryset = Person.objects.order_by('First_name')
    context_object_name = 'object_list'


class PersonUpdateView(UpdateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('app:list_person')


class PersonDetailView(DetailView):
    model = Person


class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('app:list_person')


