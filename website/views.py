from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def hello_blog(request):
	#return HttpResponse('BLOG')
	valor1 = '1'
	lista = [
		'Django', 'Python', 'Apache', 'Git', 'Html',
		'Banco de Dados ', 'Linux ', 'Nginx', 'PHP', 'CSS'
	]
	#--------------------------------
	lista_postagens = Post.objects.all()
	#------------------------------------
	data = { 'var1': valor1, 'lista_tec': lista, 'post': lista_postagens}
	
	
	return render(request, 'index.html',data)
