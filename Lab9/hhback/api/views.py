import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from . import models

def toJson(object):
    jsonObject = {}
    if(isinstance(object, models.Company)):
        jsonObject = {
            "id": object.id,
            "name": object.name,
            "description": object.description,
            "city": object.city,
            "address": object.address,
        }
    else:
        jsonObject = {
            "id": object.id,
            "name": object.name,
            "description": object.description,
            "salary": object.salary,
            "company": str(object.company),
        }

    return jsonObject

def deleteCompanies(request):
    companies = models.Company.objects.all()
    for company in companies:
        company.delete()
    return HttpResponse("All companies are deleted")

def deleteVacancies(request):
    vacancies = models.Vacancy.objects.all()
    for vacancy in vacancies:
        vacancy.delete()
    return HttpResponse("All vacancies are deleted")

@csrf_exempt
def createCompany(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        name = data.get("name", "")
        descr = data.get("description", "")
        city = data.get("city", "")
        address = data.get("address", "")
        company = models.Company.objects.create(name=name, description=descr, city=city, address=address)
        return JsonResponse(toJson(company), safe=False)
    return HttpResponse("Nothing happened")

def createVacancy(request):
    name = input("Vacancy Name? ")
    descr = input("Vacancy Descr? ")
    salary = float(input("Salary? "))
    company = models.Company.objects.get(id = 13)
    vacancy = models.Vacancy(name=name, description=descr, salary=salary, company=company)
    vacancy.save()
    return JsonResponse(toJson(vacancy), safe=False)



def getCompanies(request):
    companies = models.Company.objects.all()
    companies = [toJson(company) for company in companies]
    print("SUCCESS")
    return JsonResponse(companies, safe=False)

def getCompany(request, pk):
    companies = models.Company.objects.filter(id = pk)
    companies = [toJson(company) for company in companies]
    return JsonResponse(companies, safe=False)

def getVacanciesByCompany(request, pk):
    companies = models.Company.objects.get(id = pk)
    companies = toJson(companies)
    vacancies = models.Vacancy.objects.all()
    result = set()
    for vacancy in vacancies:
        if(vacancy.company.name == companies['name']):
            result.add(vacancy.name)
    return HttpResponse(result)

def getVacancies(request):
    vacancies = models.Vacancy.objects.all()
    vacancies = [toJson(vacancy) for vacancy in vacancies]
    return JsonResponse(vacancies, safe=False)

def getVacancy(request, pk):
    vacancy = models.Vacancy.objects.get(id = pk)
    return JsonResponse(toJson(vacancy), safe=False)

def getTopVacancies(request):
    vacancies = models.Vacancy.objects.all().order_by("-salary")
    vacancies = [toJson(vacancy) for vacancy in vacancies]
    return JsonResponse(vacancies, safe=False)