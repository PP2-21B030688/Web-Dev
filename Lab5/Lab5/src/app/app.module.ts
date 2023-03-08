import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { CategoriesCompComponent } from './categories.comp/categories.comp.component';
import { StarterComponent } from './starter/starter.component';
import { ClothesComponent } from './clothes/clothes.component';
import { SouvenirsComponent } from './souvenirs/souvenirs.component';
import { FiguresComponent } from './figures/figures.component';
import { TraditionalComponent } from './traditional/traditional.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    CategoriesCompComponent,
    StarterComponent,
    ClothesComponent,
    SouvenirsComponent,
    FiguresComponent,
    TraditionalComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
