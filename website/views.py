from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_blog(request):
	#return HttpResponse('BLOG')
	lista = [
		'Django', 'Python', 'Apache', 'Git', 'Html'
		'Banco de Dados ', 'Linux ', 'Nginx'
	]
	
	valor1 = '1'
	data = { 'var1': valor1, 'lista_tec': lista}
	
	
	return render(request, 'index.html',data)
