import { Component } from '@angular/core';
import { ApiService } from './services/api.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [HttpClientModule],  // Import HttpClientModule
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  message = '';
  name = '';
  greeting = '';

  constructor(private apiService: ApiService) {}

  sendGreeting() {
    console.log(this.name);
    this.apiService.greetUser(this.name).subscribe((response) => {
      this.greeting = response.message;
    });
  }

  updateName(event: Event){
    const inputElement = event.target as HTMLInputElement;
    this.name = inputElement.value;
  }
}
