import { Component, OnInit } from '@angular/core';
import { Quote } from '../quote';
@Component({
  selector: 'app-quote',
  templateUrl: './quote.component.html',
  styleUrls: ['./quote.component.css']
})
export class QuoteComponent implements OnInit {
	quotes = [
	new Quote("Inauma itabidi uzoee","Simple Boy","SWahili"),
	new Quote("Ooliskia wapi","Ule Msee","Says"),
	new Quote("Hardwork pays","English","Proverb"),
	new Quote("Yaliyopita si ndewle","Swahili","Proverb"),

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
    new Quote("Hardwork pays", "English", "Proverb", 0, 0, new Date(2010,6,13)),
    new Quote("Mtaka cha mvunguni sharti ainame", "Ken", "Walibora", 0, 0, new Date(2019,6,4)),
    new Quote("Tout est beau tant que tu l'impose", "Willy William", "Mozzy", 0, 0, new Date(2012,7,21)),
    new Quote("Yaliyopita si ndwele", "KIswahili", "Proverb", 0, 0, new Date(2019,8,10))
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