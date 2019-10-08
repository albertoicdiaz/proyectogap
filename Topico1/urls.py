from django.contrib import admin
from django.urls import path, include
from Questions import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.auth_login, name="login"),
    path('logout/', views.auth_logout, name="logout"),
    path('getanswer/', views.getanswer, name='getanswer'),
    path('encuesta/', views.encuesta, name='encuesta'),
    path('llenar_encuesta/', views.llenar_encuesta, name='llenar_encuesta'),
    path('analisis/', views.analisis, name='analisis'),
    path('createpersonal/', views.createpersonal, name='createpersonal'),
    path('createcompany/', views.add_company, name='createCompany'),
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
]