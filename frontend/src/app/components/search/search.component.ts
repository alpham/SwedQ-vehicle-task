import {Component, OnInit, OnDestroy} from '@angular/core';
import {ApiService} from '../../services/api.service';
import {MatTableDataSource} from '@angular/material';
import {Vehicle} from '../../models/vehicle';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit, OnDestroy {
  public listData: MatTableDataSource<Vehicle>;
  public customerName: string;
  public online: string;
  public displayedColumns: string[] = ['id', 'reg-no', 'customer', 'online'];

  private readonly intervalId: number;

  constructor(private apiService: ApiService) {
    this.intervalId = window.setInterval(() => this.applyFilter(), 10000);
  }

  ngOnInit() {
  }

  applyFilter() {
    this.apiService.search(this.customerName, this.online).subscribe(
      (vehicles: Vehicle[]) => {
        this.listData = new MatTableDataSource<Vehicle>(vehicles);
      }
    );
  }

  ngOnDestroy(): void {
    clearInterval(this.intervalId);
  }
}
