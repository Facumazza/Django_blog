from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="index"),
    path('generales/', generales, name="generales"),
    path('reviews/', reviews, name="reviews"),
    path('guias/', guias, name="guias"),
    path('Esports/', Esports, name="Esports"),
    path('estrenos/', estrenos, name="estrenos"),
    path("<slug:slug>", detallePost, name = "detalle_post"),
    path('signup/', signup, name="signup"),
    path('logout/', cerrar_sesion, name="logout"),
    path('signin/', iniciar_sesion, name="signin"),
]
