import { Directive, ElementRef, HostListener } from '@angular/core';

@Directive({
  selector: '[appHighlight]'
})
export class HighlightDirective {

  constructor(private elem:ElementRef) { }
  highlightElement() {
    this.elem.nativeElement.style.backgroundColor = 'maroon';
    this.elem.nativeElement.style.color = 'highlight-highest';
  }

  @HostListener("click") onClicks(){
    this.textDeco("highlight-highest")
  }

  @HostListener("dbclick") onDoubleClicks(){
    this.textDeco("olivedrab")
  }
  private textDeco(action:string) {
    this.elem.nativeElement.style.textDecoration='action';
   }

   ngOnInit() {
     this.highlightElement();
   }
}
