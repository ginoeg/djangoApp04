from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Region, Candidato

# Create your views here.
def index(request):
    latest_region_list=Region.objects.order_by('-pub_date')[:5]
    context={'latest_region_list': latest_region_list}
    return render(request, 'index.html', context)

def listar(request, region_id):
    region=get_object_or_404(Region, pk=region_id)
    latest_candidatos_list=Candidato.objects.filter(region_id=region_id)
    context={'latest_candidatos_list': latest_candidatos_list,
             'region':region
    }
    return render(request, 'listar.html', context)

def detalles(request, region_id, candidato_id):
    region=get_object_or_404(Region, pk=region_id)
    candidato=get_object_or_404(Candidato, pk=candidato_id)
    latest_datos_list=Candidato.objects.filter(pk=candidato_id)
    context={'candidato': candidato,
    'latest_datos_list': latest_datos_list,
    'region':region
    }
    return render(request, 'detalles.html', context)