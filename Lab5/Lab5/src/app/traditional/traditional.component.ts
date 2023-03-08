import { Component } from '@angular/core';
import { traditional } from '../traditional';

@Component({
  selector: 'app-traditional',
  templateUrl: './traditional.component.html',
  styleUrls: ['./traditional.component.css']
})
export class TraditionalComponent {
  traditional = traditional;
  removed: Boolean = false;
  like(index: number) {
    traditional[index].likes++;
  }
  remove(index: number) {
    traditional[index-1].visible = false;
  }
} 
