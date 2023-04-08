import { Component } from '@angular/core';
import { figures } from '../figures';

@Component({
  selector: 'app-figures',
  templateUrl: './figures.component.html',
  styleUrls: ['./figures.component.css']
})
export class FiguresComponent {
  figures = figures;
  removed: Boolean = false;
  like(index: number) {
    figures[index].likes++;
  }
  remove(index: number) {
    figures[index-1].visible = false;
  }
}
