import { Injectable } from '@angular/core';
import { HttpClient, withFetch } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private apiUrl = 'http://127.0.0.1:5000/api';  // Flask API URL

  constructor(private http: HttpClient) {}

  getHelloWorld(): Observable<{ message: string }> {
    return this.http.get<{ message: string }>(`${this.apiUrl}/hello`);
  }

  greetUser(name: string): Observable<{ message: string }> {
    return this.http.post<{ message: string }>(`${this.apiUrl}/greet`, { name });
  }
}
