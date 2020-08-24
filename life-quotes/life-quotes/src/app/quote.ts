export class Quote {
    showDescription: boolean;
    constructor(
        public quote: string,
        public author: string,
        public poster: string,
        public upvotes: number,
        public downvotes: number,
        public completeDate: Date,
    ){ 
        this.showDescription=false;
    }    
}
