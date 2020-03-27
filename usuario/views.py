from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from usuario.forms import UsuarioForm, CargaForm
from usuario.models import Usuario
# Create your views here.
from django.views.generic import View
from desarrollo.utileria import render_pdf
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.urls import reverse_lazy

class index(TemplateView):
    template_name = 'usuario/index.html'

class usuario_create(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('usuario_listar')

class usuario_list(ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'
    paginate_by = 7

class usuario_edit(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('usuario_listar')

class carga_edit(UpdateView):
    model = Usuario
    form_class = CargaForm
    template_name = 'usuario/carga_form.html'
    success_url = reverse_lazy('usuario_listar')

class mas_datos(View):
    def get(self, request,id_usuario):
        usuario = Usuario.objects.get(id=id_usuario)
        contexto = {'usuario':usuario}
        datos = render(request,'usuario/mas_datos.html',contexto)
        return HttpResponse(datos)

def usuario_search(request):
    buscar = request.POST.get('buscalo')
    if buscar:
        usuario=Usuario.objects.filter(dni__contains=buscar)
    else:
        usuario = Usuario.objects.all()
        paginator = Paginator(usuario, 7)
        page = request.GET.get('page')
        usuario = paginator.get_page(page)
    contexto = {'object_list': usuario}
    return render(request, 'usuario/buscar.html',contexto)
