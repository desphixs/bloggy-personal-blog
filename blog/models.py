from django.db import models

# Think of the database as a giant, highly organized digital filing cabinet.
# A Model in Django is like a blueprint or a recipe card that tells the database
# exactly how to construct a specific drawer in that cabinet and what columns/details it should hold.

class Post(models.Model):
    # This class represents a blog post.
    # Analogy: Think of a Post like a physical newspaper article. Every article needs a headline (title), 
    # the main text (content), and a stamp showing when it was published (created_at).
    
    # We use CharField for short-to-medium text. Think of this like a physical label maker that prints
    # a single line of text with a strict length limit so it fits perfectly on a folder tab.
    # Here, we limit our title to 200 characters.
    title = models.CharField(max_length=200)
    
    # We use TextField for large blocks of text that can span multiple paragraphs.
    # Analogy: Think of this as a blank, unlined piece of paper where you can write an essay
    # or a full story without worrying about running out of space.
    content = models.TextField()
    
    # We use DateTimeField to keep track of the exact date and time.
    # The 'auto_now_add=True' is like an automatic date stamp. The moment a new post is saved,
    # the database automatically stamps the current date and time on it, just like an ink stamp
    # at a post office when you mail a package.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # The __str__ method tells Django how to represent this object as a simple human-readable string.
        # Analogy: If someone asks you "Which folder is that?", you don't say "Folder ID #5439", 
        # you say "The one titled 'My First Vacation'". This method gives our post a friendly label.
        return self.title


class Comment(models.Model):
    # This class represents a reader's comment left on a blog post.
    # Analogy: Think of a comment like a sticky note that a reader attaches to a specific newspaper article.
    # You can't just have sticky notes floating around in the air; they MUST be stuck onto a specific article.
    
    # A ForeignKey creates a direct link (relationship) between this Comment and a specific Post.
    # Analogy: Think of this like a physical string connecting a sticky note to a newspaper article.
    # 'on_delete=models.CASCADE' means that if we throw away (delete) the Post, Django will automatically
    # throw away all the sticky notes (comments) attached to it as well, so we don't have orphan comments.
    # 'related_name="comments"' lets us easily ask a Post "Hey, give me a list of all your comments!"
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    # We use CharField for the commenter's name, limiting it to 100 characters.
    # Analogy: A name tag where the reader writes who they are.
    author_name = models.CharField(max_length=100)
    
    # We use TextField for the body of the comment so readers can write short or long thoughts.
    # Analogy: The message area on our sticky note.
    body = models.TextField()
    
    # Just like with the Post, this automatically stamps the exact time the comment was posted.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # A human-readable label for the comment in the admin interface.
        # Analogy: If we hold up a sticky note, we label it with who wrote it and what article it belongs to, 
        # like "Comment by Alice on 'My First Vacation'".
        return f"Comment by {self.author_name} on '{self.post.title}'"
