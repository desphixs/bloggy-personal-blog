from django.urls import path
from . import views

# We define the URL configurations for our blog app here.
# Analogy: This is like a list of room numbers and labels inside the reading room lounge.
# If a guest asks for the "homepage" (empty path), we send them to the post_list view.

urlpatterns = [
    # The empty string represents the root URL of our blog (homepage).
    # Analogy: Walking through the main entrance of the blog section.
    path('', views.post_list, name='post_list'),
    
    # Dynamic Article URL: looks for a URL pattern like "/post/5/" where 5 is the database ID.
    # Analogy: A dynamic catalog drawer number. The '<int:id>' captures the custom integer ID 
    # and forwards it to the post_detail view function so it knows exactly which article to open.
    path('post/<int:id>/', views.post_detail, name='post_detail'),
]
