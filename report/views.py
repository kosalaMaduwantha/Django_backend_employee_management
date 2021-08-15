from django.shortcuts import render
from rock_fort_backend.models import task
from django.http import JsonResponse

from django.core import serializers

# Create your views here.

def dashboard_with_pivot(request):
  return render(request, 'dashboard_with_pivot.html', {})




def pivot_data(request):
  dataset = task.objects.all()
  data = serializers.serialize('json', dataset)
  return JsonResponse(data, safe=False)

