from django.db import models
from user.models import User
from user.models import TimestampMixin

class Author(TimestampMixin):
    name = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_creator')


    def __str__(self):
        return self.name


class Book(TimestampMixin):
    title = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    availability_status = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='book_author')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='book_creator')


    class Meta:
        ordering = ('-publication_date',)

    def __str__(self):
        return self.title