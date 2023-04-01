import { Component } from '@angular/core';
import { clothes } from '../clothes';

@Component({
  selector: 'app-clothes',
  templateUrl: './clothes.component.html',
  styleUrls: ['./clothes.component.css']
})
export class ClothesComponent {
  clothes = clothes;
  removed: Boolean = false;
  like(index: number) {
    clothes[index].likes++;
  }
  remove(index: number) {
    clothes[index-1].visible = false;
  }
}
