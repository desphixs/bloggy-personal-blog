from django.shortcuts import render, get_object_or_404
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


def post_detail(request, id):
    # This view fetches a single post using its unique ID and displays its full content.
    # Analogy: Imagine the post list is like a library catalog of books. Each book has a unique barcode (the ID).
    # When a reader clicks a book title, they are asking for the full text of that specific book.
    # The waiter (our view) checks the library catalog, pulls the single book with that barcode, 
    # and opens it for the reader to browse.
    
    # We use Django's get_object_or_404 shortcut to find the exact article.
    # Analogy: Think of get_object_or_404 like a library assistant. If you ask for a book that is actually 
    # on the shelf (matches the ID), the assistant happily hands it to you. If you ask for a book that has 
    # never existed, instead of freezing or crashing the whole library (a server error), the assistant politely 
    # tells you: "Sorry, we don't have that book!" (which returns a clean 404 Page Not Found error to the user).
    post = get_object_or_404(Post, id=id)
    
    # We package our single post onto the carrying tray context dictionary.
    # Analogy: Loading the book onto the waiter's tray so it can travel into the template room (post_detail.html).
    context = {
        'post': post,
    }
    
    # Render the detailed template, mapping request, template name, and context together.
    # It fills post_detail.html with the selected post's headline, text content, and publication date.
    return render(request, 'blog/post_detail.html', context)
