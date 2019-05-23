import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Words } from './Words';
import { Quotes } from './Quotes';
import { Output } from './Output';

@Component({
  selector: 'my-app',
  templateUrl: './app.component.html',
  styleUrls: [ './app.component.css' ]
})
export class AppComponent implements OnInit {
  name = 'Angular';

  allWords: Array<Words> = []
  allQuotes: Array<Quotes> = []
  allOutputs: Array<Output> = []

  constructor(private http: HttpClient){

  }

  ngOnInit() {
    // Putting words in database
    this.http.put('http://localhost:5000/putcsv', {bool: true}).subscribe((result) => {
      this.http.put('http://localhost:5000/putcsv', {bool: false}).subscribe((res) => {
        // Now getting all words
        this.http.get('http://localhost:5000/words').subscribe((words) => {
          var temp: Array<any> = words as Array<any>
          temp.forEach((element) => {
            this.allWords.push(new Words(element["id"], element["word"]))
          })
          // Now getting all Quotes
          this.http.get('http://localhost:5000/quotes').subscribe((quotes) =>{
            var temp: Array<any> = quotes as Array<any>
            temp.forEach((quote) => {
              this.allQuotes.push(new Quotes(quote["quote_id"], quote["author"], quote["quote"]))
            })
            // Now processing.
            this.allQuotes.forEach((quote) => {
              quote.toString().split(" ").forEach((currentWord) => {
                // If allWords contains this word,
                  this.http.post('http://localhost:5000/word/', {word: currentWord}).subscribe((frequencyOfWord) => {
                    // Creating output variable.
                    var test: Output = new Output(currentWord, frequencyOfWord["result"])
                    // If word not in allOutputs
                    if(!(this.allOutputs.indexOf(test) > -1)) {
                      // Add to allOutputs
                      this.allOutputs.push(test)
                    }
                  })
              })
            })
            // Done!
          })
        })
      })
    })
  }

}
