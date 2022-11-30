from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import File
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
from django.db.models import Avg


class HomeViewIris(View):  # definimos a classe HomeView que será chamada dentro do urls.py
    # esta classe fará que, quando requisitada (pela homepage da nossa aplicação web) seja renderizado o index.html (que está dentro de irisjs)
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class ListIris(APIView):  # criamos a classe que permitirá a criação da API
    authentication_classes = []
    permission_classes = []

    # definimos o que esta classe irá retornar no API quando for requisitada (a estrutura dos dados)
    def get(self, request, format=None):
        # neste caso, será criada uma variável 'species' em que estarão o nome das espécies de todas as linhas do nosso banco de dados (File)
        species = [iris.species for iris in File.objects.all()]
        # mesma coisa que o anterior, mas para o comprimento da sépala
        sepalLn = [iris.sepal_length for iris in File.objects.all()]
        # mesma coisa que o anterior, mas para a largura da sépala
        sepalWd = [iris.sepal_width for iris in File.objects.all()]
        # neste caso, estamos selecionando apenas os valores únicos de espécies
        speciesUnique = File.objects.values_list(
            'species', flat=True).distinct()
        spCount = File.objects.values('species').annotate(average_rating=Avg(
            'sepal_length')).values_list('average_rating', flat=True)
        spScatter = [{'x': iris.sepal_length, 'y': iris.sepal_width}
                     for iris in File.objects.all()]
        data = {"species": species, "sepalLn": sepalLn, "sepalWd": sepalWd,
                'spUni': speciesUnique, 'spCount': spCount, 'spScatter': spScatter}
        return Response(data)
