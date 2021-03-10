import { Component, Input } from '@angular/core';
import { ConfigService } from './config/config.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
// import { HttpClient, HttpErrorResponse,  } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private http: HttpClient) { }
  error: any;
  confff = ConfigService
  tickets: any;
  acceso = 'false';


  urlAPILogin(username,password){
    const headers = { 'content-type': 'application/json'}
    const body=JSON.stringify({'username':username,'password':password});
    return this.http.post('http://localhost:81/api-token-auth/?'
                          , body, {'headers':headers}
                        );
  }

  urlAPI(palabra,select,id_ticket){
    let httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        Authorization: "Token " + this.acceso
      })
    };
    return this.http.get('http://localhost:81/sistemasexpertos/tickets/?'
                          + (Boolean(id_ticket) ? ('&id='+id_ticket) : '')
                          + (Boolean(select) ? ('&estado='+select) : '')
                          + (Boolean(palabra) ? ('&palabra='+palabra) : '')
                          , httpOptions
                        );
  }
  getList(palabra,select,id_ticket){
    this.urlAPI(palabra,select,id_ticket).subscribe(
      data => {
        this.tickets = data;
      },
      err => {
        this.error="Error: Intenta revisar si iniciaste sesión.";
        console.error(err);
      },
      () => console.log("*")
    );
  }
  getToken(username,password){
    this.urlAPILogin(username,password).subscribe(
      data => {
        this.acceso = data['token'];
        this.error = "";
      },
      err => {
        this.error="Fallo de inicio de sesión. Vuelve a intentarlo.";
        console.error(err);
      },
      () => console.log("*")
    );
  }



  // falla
  // createPost(){alert(ConfigService.x.toString())}

  // work
  // createPost(){alert(ConfigService.toString())}

  // work
  // createPost(){alert(this.confff.toString());}

  showHeroes = true;
  toggleHeroes() { this.showHeroes = !this.showHeroes; }


}
