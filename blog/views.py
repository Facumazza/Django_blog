from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def home(request):
    posts_queryset = Post.objects.filter(estado = True).order_by('-fecha_publicacion')
    queryset = request.GET.get("buscar")
    if queryset:
        posts_queryset = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts_queryset, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, "index.html", {"posts":posts})

def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "signup.html", {"form": form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                return redirect("blog:index")
            except IntegrityError:
                return render(request, "signup.html", {"form": form, "error": "El nombre de usuario ya existe"})
        else:
            return render(request, "signup.html", {"form": form, "error": "Contraseña incorrecta"})
    
    
def cerrar_sesion(request):
    logout(request)
    return redirect('blog:index') 

def iniciar_sesion(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm()})
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("blog:index")
        else:
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, "signin.html", {"form": form, "error": error_message})
        

def detallePost(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, "post.html", {"detalle_post":post})

def generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = "Generales")).order_by('-fecha_publicacion')
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Generales'),
        ).distinct()
        
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, "generales.html", {"posts":posts})

def reviews(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        
        estado = True, 
        categoria = Categoria.objects.get(nombre__iexact = "Reviews")).order_by('-fecha_publicacion') 

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Reviews'),
        ).distinct()
    
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, "reviews.html", {"posts":posts})

def guias(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = "Guias")).order_by('-fecha_publicacion') 
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Guias'),
        ).distinct()
    
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, "guias.html", {"posts":posts})

def estrenos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = "Estrenos")).order_by('-fecha_publicacion') 
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Estrenos'),
        ).distinct()
    
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, "estrenos.html", {"posts":posts})

def Esports(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = "Esports")).order_by('-fecha_publicacion') 
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Esports'),
        ).distinct()
    
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, "Esports.html", {"posts":posts})