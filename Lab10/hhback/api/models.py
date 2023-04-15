from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

    def updateCompany(self, data):
        self.name = data.get("name", "")
        self.description = data.get("description", "")
        self.city = data.get("city", "")
        self.address = data.get("address", "")
        self.save()
    
    def deleteCompany(self):
        messageBody = "Company '" + self.name + "' with ID " + str(self.id) + " has been deleted!"
        self.delete()
        return messageBody

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-salary"]

    def __str__(self):
        return self.name
    
    def updateVacancy(self, data):
        try:
            company = Company.objects.get(name=data.get("company", ""))
            self.name = data.get("name", "")
            self.description = data.get("description", "")
            self.salary = data.get("salary", "")
            self.company = company
            self.save()
        except Company.DoesNotExist as error:
            return False
        
        return True

    def deleteVacancy(self):
        message = "Vacancy '" + self.name + "' with ID " + str(self.id) + " has been deleted"
        self.delete()
        return message