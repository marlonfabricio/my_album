from django.conf.urls import url
from django.contrib import admin
from album import views

urlpatterns = [
	# $ SIGNIFICA QUE LLEGUE LA IP SIN NINGUN MODIFICADOR
	url(r'^$', views.first_view, name="first-view"),
	# Haciendo referencia a la vista category
	url(r'^category/$', views.category, name="category-list"),
	# Recibiendo un parámetro numérico [0-9]
	url(r'^category/(?P<category_id>[0-9]+)/detail/$', views.category_detail, name="category-detail"),
	url(r'^photo/$', views.PhotoListView.as_view(), name="photo-list"),
	url(r'^photo/(?P<pk>[0-9]+)/detail/$', views.PhotoDetailView.as_view(), name="photo-detail"),
]