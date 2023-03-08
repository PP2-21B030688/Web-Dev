import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CategoriesCompComponent } from './categories.comp/categories.comp.component';
import { StarterComponent } from './starter/starter.component';
import { ClothesComponent } from './clothes/clothes.component';
import { SouvenirsComponent } from './souvenirs/souvenirs.component';
import { FiguresComponent } from './figures/figures.component';
import { TraditionalComponent } from './traditional/traditional.component';

const routes: Routes = [
  {
    path: "categories", component: CategoriesCompComponent,
  },
  {
    path: "", component: StarterComponent,
  },
  {
    path: "clothes", component: ClothesComponent,
  },
  {
    path: "souvenirs", component: SouvenirsComponent,
  },
  {
    path: "traditional", component: TraditionalComponent,
  },
  {
    path: "figures", component: FiguresComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
