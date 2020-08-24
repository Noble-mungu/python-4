import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Quote } from '../quote';
import { DateCountPipe } from '../date-count.pipe';

@Component({
  selector: 'app-quote-detail',
  templateUrl: './quote-detail.component.html',
  styleUrls: ['./quote-detail.component.css']
})
export class QuoteDetailComponent implements OnInit {

  @Input() quote: Quote;
  @Output() isComplete = new EventEmitter<boolean>();

  quoteDelete(complete:boolean){
    this.isComplete.emit(complete);
  }
  
  upvote(){
    this.quote.upvotes = this.quote.upvotes +1;
  }
  downvote(){
    this.quote.downvotes = this.quote.downvotes +1;
  }
  constructor() { }

  ngOnInit(): void {
  }

}
