from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

import logging
logger = logging.getLogger('django')


from .models import *
from .serializers import *

# Create your views here.
class BookListView(APIView):
    try:
        def get(self, request):
            book = Book.objects.all()
            serializer = BookSerializer(book, many=True)
            return JsonResponse(serializer.data, safe=False)
        
        def post(self, request):
            book = BookSerializer(request.data)
            if book.is_valid():
                book.save()
                return JsonResponse(book.data, status=status.HTTP_201_CREATED )
            return JsonResponse(book.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as err:
        logger.error('error in Booklistview' + str(err))
        raise Response.internal_server_error(err)


