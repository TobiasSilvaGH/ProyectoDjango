from django.shortcuts import get_object_or_404, render


#El segundo argumento lo tengo que aclarar en las urls "admin_blog_id"
def index(request):
	#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
	#'-pub_date' le designo un programador/ es un atributo de el modelo
    
    return render(request, 'secciones/index.html')