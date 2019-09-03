import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Router } from '@angular/router';

export interface PeriodicElement {
  contact: string;
  position: number;
  code: number;
  result: string;
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  ELEMENT_DATA: PeriodicElement[] = [
    {position: 1, contact: 'Hydrogen', code: 1.0079, result: 'H'},
    {position: 2, contact: 'Helium', code: 4.0026, result: 'He'},
    {position: 3, contact: 'Lithium', code: 6.941, result: 'Li'},
    {position: 4, contact: 'Beryllium', code: 9.0122, result: 'Be'},
    {position: 5, contact: 'Boron', code: 10.811, result: 'B'},
    {position: 6, contact: 'Carbon', code: 12.0107, result: 'C'},
    {position: 7, contact: 'Nitrogen', code: 14.0067, result: 'N'},
    {position: 8, contact: 'Oxygen', code: 15.9994, result: 'O'},
    {position: 9, contact: 'Fluorine', code: 18.9984, result: 'F'},
    {position: 10, contact: 'Neon', code: 20.1797, result: 'Ne'},
  ];

  displayedColumns: string[] = ['position', 'contact', 'code', 'result'];
  dataSource = this.ELEMENT_DATA;
  
  findParams = [{
    email: "",
    password: ""
  }]

  users: Object;

  constructor(private data: DataService, private router: Router) { }

  ngOnInit() {
    this.findParams[0].email = localStorage.getItem('email');
    this.findParams[0].password = localStorage.getItem('password');

    //CHECK IF USER IS LOGGED
    var manualRouter = this.router;
    //Search a new user in db, maybe he is exist there 
    var findCheker = this.data.findOwnerByEmail(this.findParams);
    findCheker.onreadystatechange = function() {

      //Check if responce status is 200
      if (this.readyState == 4 && this.status == 200) {

        //Get a result about user
        var answer = JSON.parse(findCheker.response);

        if(answer.result !== 'user exists'){

          //redirect to login
          manualRouter.navigate(['/login']);
        }
      }
     
    };
  }

}
