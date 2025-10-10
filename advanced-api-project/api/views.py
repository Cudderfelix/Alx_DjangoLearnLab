# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer

@api_view(['GET'])
def list_authors(request):
    """Returns a list of authors with their books."""
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)