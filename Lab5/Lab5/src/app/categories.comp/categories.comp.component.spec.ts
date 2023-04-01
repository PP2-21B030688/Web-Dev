import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CategoriesCompComponent } from './categories.comp.component';

describe('CategoriesCompComponent', () => {
  let component: CategoriesCompComponent;
  let fixture: ComponentFixture<CategoriesCompComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CategoriesCompComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CategoriesCompComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
