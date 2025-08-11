from django.shortcuts import render, redirect
from .models import Cursos
from django.shortcuts import get_object_or_404
from .forms import CursosForm

# Create your views here.
def cursos(request):
    cursos=Cursos.objects.all()
    
    return render(request, "cursos/cursos.html",{'cursos':cursos})

def registrar(request):
    if request.method == 'POST':
        form = CursosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Cursos")
    else:
        form = CursosForm()
    
    return render(request, 'cursos/agregar_curso.html', {'form': form})



def eliminarCurso(request, id, confirmacion='cursos/confirmarEliminacion.html'):
    curso = get_object_or_404(Cursos, id=id)
    if request.method == 'POST':
        curso.delete()
        cursos = Cursos.objects.all()
        return render(request, "cursos/cursos.html", {'cursos': cursos})
    return render(request, confirmacion, {'object': curso})

def editarCurso(request, id):
    curso = get_object_or_404(Cursos, id=id)
    form = CursosForm(request.POST, instance=curso)
    if form.is_valid():
        form.save()
        cursos=Cursos.objects.all()
        return render(request, "cursos/cursos.html", {'cursos':cursos})
    

def consultarCursoIndividual(request, id):
    curso = get_object_or_404(Cursos, id=id)
    return render(request, "cursos/formEditarCurso.html", {'curso': curso})