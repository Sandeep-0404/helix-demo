from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import QuestionSerializer
from .models import Questions

# Create your views here.

@api_view(['GET'])
def apiOverview(response):
    api_urls={
        'List':'/list',
        'Post':'/post'
    }

    return Response(api_urls)


@api_view(['GET','POST'])
def Post(response):
    if response.method == 'GET':
        post=Questions.objects.all()
        serializer=QuestionSerializer(post,many=True)
        return Response(serializer.data)
    
    elif response.method == 'POST':
        serializer=QuestionSerializer(data=response.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)