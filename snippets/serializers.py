# snippets/serializers.py

from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet #snippet-ის თეიბლის სვეტებს ვუთითებთ
        fields = (
            "id",
            "title",
            "code",
            "linenos",
            "language",
            "style",
        )