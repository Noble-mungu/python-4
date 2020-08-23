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

  constructor() { }
  completeQuote(isComplete,index){
  	if (isComplete){
  		this.quotes.splice(index,1);
  	}
  }
  toggleDetails(index){
  	this.quote[index].shoeDescription = !this.quotes[index].showDescription;
  }

  ngOnInit(): void {
  }

}
