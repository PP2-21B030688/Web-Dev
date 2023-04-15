import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . import serializing
from . import models

@csrf_exempt
def getCompanies(request):
    if(request.method == "GET"):
        companies = models.Company.objects.all()
        serializer = serializing.CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == "POST"):
        data = json.loads(request.body)
        name = data.get("name", "")
        description = data.get("description", "")
        city = data.get("city", "")
        address = data.get("address", "")
        newCompany = models.Company.objects.create(name=name, description=description, city=city, address=address)
        serializer = serializing.CompanySerializer(newCompany)
        return JsonResponse(serializer.data)

    return HttpResponse("Unknown request has been triggered")

@csrf_exempt
def getCompany(request, pk):
    try:
        company = models.Company.objects.get(id=pk)
    except models.Company.DoesNotExist as error:
        return JsonResponse({"error": error}, status=400)
    
    if(request.method == "GET"):
        serializer = serializing.CompanySerializer(company)
        return JsonResponse(serializer.data)
    elif(request.method == "PUT"):
        data = json.loads(request.body)
        company.updateCompany(data)
        serializer = serializing.CompanySerializer(company)
        return JsonResponse(serializer.data)
    elif(request.method == "DELETE"):
        message = company.deleteCompany()
        return JsonResponse({"message": message})

@csrf_exempt
def getVacanciesByCompany(request, pk): # id of company
    try:
        company = models.Company.objects.get(id=pk)
    except models.Company.DoesNotExist as error:
        return JsonResponse({"message": "Such company doesn't exist..."})
    
    vacancies = models.Vacancy.objects.filter(company__id=pk).values()
    return HttpResponse(vacancies) #????

@csrf_exempt
def getVacancies(request):
    if(request.method == "GET"):
        vacancies = models.Vacancy.objects.all()
        serializer = serializing.VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == "POST"):
        data = json.loads(request.body)
        name = data.get("name", "")
        descr = data.get("description", "")
        salary = data.get("salary", "")
        companyName = data.get("company", "")

        try:
            company = models.Company.objects.get(name=companyName)
        except models.Company.DoesNotExist as error:
            return JsonResponse({"message": str(error)})
        
        newVacancy = models.Vacancy.objects.create(name=name, description=descr, salary=salary, company=company)
        serializer = serializing.VacancySerializer(newVacancy)
        return JsonResponse(serializer.data)
    
@csrf_exempt
def getVacancy(request, pk):
    try:
        vacancy = models.Vacancy.objects.get(id=pk)
    except models.Vacancy.DoesNotExist as error:
        return JsonResponse({"message": str(error)})
    
    if(request.method == "GET"):
        serializer = serializing.VacancySerializer(vacancy)
        return JsonResponse(serializer.data)
    elif(request.method == "PUT"):
        data = json.loads(request.body)
        if(vacancy.updateVacancy(data)): # succesful update
            serializer = serializing.VacancySerializer(vacancy)
            return JsonResponse(serializer.data)
        return JsonResponse({"message": "Such company doesn't exist..."})
    elif(request.method == "DELETE"):
        message = vacancy.deleteVacancy()
        return JsonResponse({"message": message})
    
@csrf_exempt
def getTopTenVacancies(request):
    if(request.method == "GET"):
        vacancies = models.Vacancy.objects.all().order_by("-salary")[:10]
        serializer = serializing.VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
