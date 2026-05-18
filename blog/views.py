from django.shortcuts import render
from .models import Post

# A View in Django is like a friendly waiter in a high-end restaurant.
# 1. You (the client) sit at the table and ask the waiter for a specific menu item (the URL request).
# 2. The waiter (the view function) walks to the kitchen (the database/models) to fetch the ingredients (blog posts).
# 3. The waiter then takes those ingredients to the chef, who plates them beautifully (the HTML template).
# 4. Finally, the waiter brings the delicious, complete plate back to your table (the HTTP response).

def post_list(request):
    # This view fetches all blog posts and shows them on the homepage.
    # Analogy: Think of the homepage like a physical bulletin board where we pin index cards of all our blog posts.
    
    # We query the database to fetch all Post objects.
    # We order them by 'created_at' in descending order (with the minus sign '-'), 
    # meaning the newest articles appear at the top, just like a modern social feed.
    posts = Post.objects.all().order_by('-created_at')
    
    # We package our posts inside a Python dictionary called 'context'.
    # Analogy: Think of the context dictionary like a server's tray. We load our fetched posts 
    # onto this tray so the waiter can carry them safely into the template room (post_list.html).
    context = {
        'posts': posts,
    }
    
    # Finally, we render the template.
    # The render function takes the original request, finds the HTML template file, 
    # and fills it with our context data (replacing placeholders with real post titles and dates).
    # Then it ships the completed web page back to the user's browser.
    return render(request, 'blog/post_list.html', context)
