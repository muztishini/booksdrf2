from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Books


class BookViewSets(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('id')
    serializer_class = BookSerializer
