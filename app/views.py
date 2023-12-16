from django.shortcuts import render
from app.models import *
# Create your views here.
def display_country(request):
    QLCO=Country.objects.all()
    d={'QLCO':QLCO}
    return render(request,'display_country.html',d)
def display_capital(request):
    QLCO=Capital.objects.all()
    d={'QLCO':QLCO}
    return render(request,'display_capital.html',d)
def insert_country(request):
    cn=input('Enter country Name :- ')
    CO=Country.objects.get_or_create(country_name=cn)[0]
    CO.save()
    QLCO=Country.objects.all()
    d={'QLCO':QLCO}
    return render(request,'display_country.html',d)
def insert_capital(request):
    cn=input('Enter country Name :- ')
    c=input('Enter Capital Name :- ')
    CO=Country.objects.get(country_name=cn)
    C=Capital.objects.get_or_create(country_name=CO,city_name=c)[0]
    C.save()
    QLCO=Capital.objects.all()
    d={'QLCO':QLCO}
    return render(request,'display_capital.html',d)
