import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'data-holder',
  template: `
    <span id="hello"> Word: {{word}}, Frequency: {{frequency}} </span>
  `
})
export class DataHolderComponent implements OnInit {
  // Removed the div so that it comes in the same line lol.
  name = 'DataHolder';

  @Input('word') word: string = "None"

  @Input('freq') frequency: number = 0

  ngOnInit() {
    // Gonna put code here to change the font size
    // according to the frequency later
    var span = document.getElementById("hello")
    var size = this.frequency.toString()+"px";
    span.style.fontSize = size;
  }

}