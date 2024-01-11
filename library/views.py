from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer,AuthorSerializer
from .models import Book, Author


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'bio']

class AuthorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['availability_status', 'publication_date']
    search_fields = ['title']

    def perform_create(self, serializer):

        authors_data = self.request.data.get('authors', [])
        book = serializer.save()
        for author_data in authors_data:
            author = Author.objects.get(pk=author_data['id'])
            book.authors.add(author)

class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):

        authors_data = self.request.data.get('authors', [])
        book = serializer.save()
        book.authors.clear()
        for author_data in authors_data:
            author = Author.objects.get(pk=author_data['id'])
            book.authors.add(author)
