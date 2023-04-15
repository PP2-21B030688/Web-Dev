import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";

import { Vacancy } from './company/vacancies';

@Injectable({
  providedIn: 'root'
})
export class VacanciesService {

  constructor(private http : HttpClient) { }

  getVacancies(): Observable<Vacancy[]> {
    return this.http.get('http://127.0.0.1:8000/api/vacancies/') as Observable<Vacancy[]>;
  }
}
