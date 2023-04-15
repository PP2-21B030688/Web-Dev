import { Component } from '@angular/core';

import { Vacancy } from '../company/vacancies';
import { VacanciesService } from '../vacancies.service';

@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.css']
})
export class VacanciesComponent {
	vacancies: Vacancy[] = []

	constructor(private vacanciesService : VacanciesService) {}

	ngOnInit() {
		this.vacanciesService.getVacancies().subscribe((vacancies) => this.vacancies = vacancies); 
	}
}
