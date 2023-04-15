import { Component, OnInit } from '@angular/core';

import { Company } from './companies';
import { CompanyServiceService } from '../companies.service';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit {
	companies: Company[] = []

	constructor(private companiesService: CompanyServiceService) { }

	ngOnInit() {
		this.companiesService.getCompanies().subscribe((companies) => this.companies = companies);
		console.log(this.companies)
	}
	
}
