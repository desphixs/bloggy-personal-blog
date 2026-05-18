from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

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
    
    # We check if the guest has sent us data (a POST request) instead of just viewing the page (a GET request).
    # Analogy: If you just walk into a diner, you are looking at the menu (GET). But if you write an order on a slip 
    # and hand it to the chef, you are posting new instructions (POST).
    if request.method == 'POST':
        # We extract the submitted form inputs directly from the request.POST tray.
        # Analogy: Reaching into the order envelope and pulling out the slip showing 'author_name' and 'body'.
        author_name = request.POST.get('author_name')
        body = request.POST.get('body')
        
        # If both fields are filled out, we create a new Comment record in the database drawer.
        # Analogy: Creating a new sticky note using the form inputs, physically tying it to the current Post book, 
        # and pinning it down so it is stored permanently.
        if author_name and body:
            Comment.objects.create(
                post=post,
                author_name=author_name,
                body=body
            )
            
        # Finally, we perform a Redirect to reload the exact same article details page.
        # Analogy: Instead of serving the customer an empty plate or leaving them stranded, the waiter 
        # spins them around and reseats them at the exact same table with a fresh, updated plate containing their new comment!
        return redirect('post_detail', id=post.id)
    
    # Using our reverse database relationship, we fetch all comments linked to this specific blog post.
    # Analogy: Imagine each post book is physically tied by strings to several yellow sticky notes (comments).
    # Since we set up `related_name='comments'` in our Comment model, we can simply grab our post book 
    # and pull the strings (`post.comments`) to get every sticky note attached to it!
    # We sort them by 'created_at' in ascending order so that comments read naturally from oldest to newest.
    comments = post.comments.all().order_by('created_at')
    
    # We package our single post and its linked comments onto the carrying tray context dictionary.
    # Analogy: Loading both the book and the box of attached sticky notes onto the waiter's tray 
    # so they can travel together into the template room (post_detail.html).
    context = {
        'post': post,
        'comments': comments,
    }
    
    # Render the detailed template, mapping request, template name, and context together.
    # It fills post_detail.html with the selected post's headline, text content, and publication date.
    return render(request, 'blog/post_detail.html', context)
