from django.contrib import admin
from django.urls import path, include

from usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    # path('cadastro/', views.cadastro, name='cadastro')
]
