import { Component } from '@angular/core';
import { souvenirs } from '../souvenirs';

@Component({
  selector: 'app-souvenirs',
  templateUrl: './souvenirs.component.html',
  styleUrls: ['./souvenirs.component.css']
})
export class SouvenirsComponent {
  souvenirs = souvenirs;
  removed: Boolean = false;
  like(index: number) {
    souvenirs[index].likes++;
  }
  remove(index: number) {
    souvenirs[index-1].visible = false;
  }
}
