from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def authors(request):
    return Response({
        "Juan David Campuzano Díaz": "338832",
        "Yuly Dayana Rodriguez": "305314",
        "Juan Diego Lemus": "243911"
    })
