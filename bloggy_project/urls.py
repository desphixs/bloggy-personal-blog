"""
URL configuration for bloggy_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include

# The project's master URL configuration.
# Analogy: Think of this like the main directories sign at the entrance of a shopping mall.
# It points to 'admin/' for the security room, and maps the entire root level to our 'blog' app URLs 
# so guests are automatically greeted by our blog app when they walk in.

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include all paths from our blog application's local urls.py file
    path('', include('blog.urls')),
]
