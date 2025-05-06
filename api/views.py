from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Author  # Import the Author model

@api_view(['GET'])
def authors(request):
    authors = Author.objects.all()  # Query all authors from the database
    authors_data = {author.name: author.code for author in authors}  # Create a dictionary of authors
    return Response(authors_data)
