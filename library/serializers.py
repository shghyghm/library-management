from rest_framework import serializers
from .models import Author, Book
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance



class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        authors_data = validated_data.pop('authors', [])
        book = Book.objects.create(**validated_data)

        for author_data in authors_data:
            author = Author.objects.create(**author_data)
            book.authors.add(author)

        return book

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.availability_status = validated_data.get('availability_status', instance.availability_status)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.user = validated_data.get('user', instance.user)
        instance.save()

        authors_data = validated_data.get('authors', [])
        instance.authors.all().delete()

        for author_data in authors_data:
            author = Author.objects.create(**author_data)
            instance.authors.add(author)

        return instance
