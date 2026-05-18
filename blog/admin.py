from django.contrib import admin
from .models import Post, Comment

# The Django Admin interface is like a powerful, visual control dashboard.
# By default, Django hides our models from this dashboard to keep it clean.
# We must explicitly "register" our models to make them visible and editable 
# inside this dashboard.

# Analogy: Think of the Admin dashboard like a security guard's monitor room. 
# If we don't register our Post and Comment models, they are like rooms without 
# cameras—the guard (admin) cannot see what is inside them. By registering them, 
# we turn on the video feed so we can view, add, edit, and delete them visually.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # This class lets us customize how the Post model is displayed in the list view.
    # Analogy: Instead of just seeing a folder name, we want a neat spreadsheet 
    # that shows the title and the date it was created side by side.
    list_display = ('title', 'created_at')
    
    # We can also add search functionality so we can easily search posts by title.
    # Analogy: A quick-search bar at the top of a spreadsheet to filter rows.
    search_fields = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # We customize how Comments are displayed.
    # Analogy: Showing the author's name, the associated post, and the comment date 
    # in columns so we can quickly moderate them.
    list_display = ('author_name', 'post', 'created_at')
    
    # Let's add a filter so we can see comments by author or post easily.
    # Analogy: A filter sidebar where we can click "Show only comments by Alice".
    list_filter = ('created_at', 'post')
    
    # Let's make it searchable by author name and comment body.
    search_fields = ('author_name', 'body')
