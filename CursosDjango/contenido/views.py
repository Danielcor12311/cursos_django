from django.shortcuts import render, HttpResponse

# Create your views here.

menu = """
<nav>
    <a href="/">Inicio</a> 
    <a href="/cursos/">Cursos</a> 
    <a href="/contacto/">Contacto</a>
</nav>
"""

def principal(request):
    return render(request, "contenido/principal.html")

def cursos(request):
    return render(request, "contenido/cursos.html")

def contacto(request):
    return render(request, "contenido/contacto.html")
