from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def authors(request):
    return Response({
        "Juan David Campuzano Díaz": "338832",
        "Yuly": "123456",
        "Juan Diego Lemus": "654321"
    })
