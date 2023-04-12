from django.shortcuts import render
from .spacyScrapperModel import spacy_model_function
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from rest_framework.response import Response

# Create your views here.


class resumeparser(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file = request.data['File']
        df = spacy_model_function(file)   
        return Response({"msg": "resume parsed successfully successfully","result":df})

