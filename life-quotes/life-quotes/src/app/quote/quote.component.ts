import { Component, OnInit } from '@angular/core';
import { Quote } from '../quote';
@Component({
  selector: 'app-quote',
  templateUrl: './quote.component.html',
  styleUrls: ['./quote.component.css']
})
export class QuoteComponent implements OnInit {
	quotes = [
	new Quote("Inauma itabidi uzoee","Simple Boy","SWahili",0,0,new Date(2013,5,5)),
	new Quote("Ooliskia wapi","Ule Msee","Says",0,0,new Date(2010,4,3)),
	new Quote("Hardwork pays","English","Proverb",0,0, new Date(2015,6,6)),
	new Quote("Yaliyopita si ndewle","Swahili","Proverb",new Date(2017,3,2)),

	]

  constructor() {}

  completeQuote(isComplete, index){
    if (isComplete) {
      this.quotes.splice(index,1);
    }
  }

  toggleDetails(index){
    this.quotes[index].showDescription = !this.quotes[index].showDescription;
  }

  quoteModel: Quote

  showNew: boolean = false;

  submitType = 'save';

   quote = [
   new Quote("Inauma itabidi uzoee","Simple Boy","SWahili",0,0,new Date(2013,5,5)),
	new Quote("Ooliskia wapi","Ule Msee","Says",0,0,new Date(2010,4,3)),
	new Quote("Hardwork pays","English","Proverb",0,0, new Date(2015,6,6)),
	new Quote("Yaliyopita si ndewle","Swahili","Proverb",new Date(2017,3,2)),

  ];

  deleteQuote(isComplete, index){
    if (isComplete) {
      let toDelete = confirm(`Are you sure you want to delete ${this.quotes[index].quote}?`)

      if (toDelete){
        this.quotes.splice(index,1)
      }
    }
  }

  onNew() {
    this.quoteModel = new Quote('', '', '', 0, 0, new Date());
    this.showNew = true;
    this.submitType = 'save';
  }
  onSave() {
    if (this.submitType === 'save') {
      this.quotes.push(this.quoteModel);
    }
    this.showNew = false;
  }
  onCancel() {
    this.showNew = false;
  }
  delete(i) {
    this.quotes.splice(i, 1);
  }

  addNewQuote(quote){
    let quoteLength = this.quotes.length;
    quote.id = quoteLength+1;
    quote.completeDate = new Date(quote.completeDate)
    this.quotes.push(quote)
  }

  ngOnInit(): void {
  }

}