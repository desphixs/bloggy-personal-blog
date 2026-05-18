from django.urls import path
from . import views

# We define the URL configurations for our blog app here.
# Analogy: This is like a list of room numbers and labels inside the reading room lounge.
# If a guest asks for the "homepage" (empty path), we send them to the post_list view.

urlpatterns = [
    # The empty string represents the root URL of our blog (homepage).
    # Analogy: Walking through the main entrance of the blog section.
    path('', views.post_list, name='post_list'),
]
