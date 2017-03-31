from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category,Photo
from django.views.generic import ListView,DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.
def first_view(request):
	"""Método para renderizar base.html"""
	return render(request, 'base.html')

def category(request):
	"""Metodo para renderizar category.html"""
	# Category.objects.all() -> SELECT * FROM category
	category_list=Category.objects.all()
	context={'object_list':category_list}
	return render(request, 'album/category.html', context)

def category_detail(request, category_id):
	"""Metodo para renderizar category_detail.html"""
	# Category.objects.get(id=category_id) -> SELECT * FROM category WHERE id=category_id
	category=Category.objects.get(id=category_id)
	context={'object':category}
	return render(request, 'album/category_detail.html', context)

class PhotoListView (ListView):
	model=Photo

class PhotoDetailView(DetailView):
	model=Photo

class PhotoUpdate(UpdateView):
	model = Photo
	fields = '__all__'

class PhotoCreate(CreateView):
	model=Photo
	fields = '__all__'

class PhotoDelete(DeleteView):
	model=Photo
	success_url=reverse_lazy('photo-list')