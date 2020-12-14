from django.shortcuts import render
from .models import Certificate
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from .models import Certificate

# Create your views here.
def multimeter(request):
	return render(request, 'multimeter_format.html')

class CertificateList(ListView):
	model = Certificate
	template_name = 'list_view.html'

class CertificateDetail(DetailView): 
    model = Certificate
    template_name = 'detail_view.html'
