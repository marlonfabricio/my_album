from django.db import models


class Category(models.Model):
    """ Categorias para clasificar las fotos """
    name = models.CharField(max_length=50)
    def __str__(self):             
        return self.name

class Photo(models.Model):
	"""Fotos del album"""
	category=models.ForeignKey(Category,null=True,blank=True)
	title=models.CharField(max_length=50,default='No title')
	photo=models.ImageField(upload_to='photos/')
	pub_date=models.DateField(auto_now_add=True)
	favorite=models.BooleanField(default=False)
	comment=models.CharField(max_length=200,blank=True)
	def __str__(self):
		return self.title

class Estudiante(models.Model):
	"""Estudiantes"""
	email=models.EmailField(max_length=254)
	nombres=models.CharField(max_length=50)
	apellidos=models.CharField(max_length=50)
	direccion=models.CharField(max_length=100)
	fecha_nac=models.DateField(auto_now_add=False)
	observaciones=models.TextField(max_length=500)