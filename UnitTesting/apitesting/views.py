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


class BookDetailView(APIView):
    try:

        def get(self, request):

            pk = request.query_params.get('pk')
            book = get_object_or_404(Book, pk=pk)
            serializer = BookSerializer(book)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        
        def put(self, request):

            pk = request.query_params.get('pk')
            book = get_object_or_404(Book, pk=pk)
            serializer = BookSerializer(book, request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request):
            pk = request.query_params.get('pk')
            book = get_object_or_404(Book, pk=pk)
            book.delete()
            return JsonResponse({'message':'book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as err:
        logger.error('error in BookDetailView' + str(err))
        raise Response.internal_server_error(err)