import { Component } from '@angular/core';
import { ActivatedRoute } from "@angular/router";

import { Vacancy } from './vacancies';
import { VacanciesService } from '../vacancies.service';
import { CompanyServiceService } from '../companies.service';
import { Company } from '../companies/companies';

@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css']
})
export class CompanyComponent {
	vacancies: Vacancy[] = [];
	companies: Company[] = [];
	company: Company;
	companyID: number = 0;

	constructor(private route: ActivatedRoute, 
				private vacanciesService: VacanciesService, 
				private companiesService: CompanyServiceService,) {
					this.company = {} as Company;
				}

	ngOnInit() {
		const routeParams = this.route.snapshot.paramMap;
		const companyParamID = Number(routeParams.get("id"));
		this.companyID = companyParamID;
		this.vacanciesService.getVacancies().subscribe((vacancies: Vacancy[]) => 
			this.vacancies = vacancies.filter(vacancy => vacancy.company === companyParamID));

		this.companiesService.getCompanies().subscribe((companies: Company[]) => this.companies = companies);
			
		// this.companies = companies.filter(company => company.id === companyParamID));
	}

	correctCompany(vacancy: Vacancy, id: number): Boolean{
		if(vacancy.company === id) {
			return true
		}
		return false
	}
}
