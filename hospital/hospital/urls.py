"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.home ,name="home"),
    
    path("Jai_baba/",views.jai_baba_ki,name="Baba"),

    path('admin/', admin.site.urls),

    path('html/', views.html,name="html"),
    
    path('html1/', views.html_1,name="html_1"),
    
    path('html2/', views.html_2,name="html_2"),
    
    path('html3/', views.html_3,name="html_3"),

    path('html4/', views.html_4,name="html_4"),
]
