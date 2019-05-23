export class Quotes {

  quote_id: number;
  author: string;
  quote: string;

  constructor(qID: number, auth: string, quot: string) {
    this.quote_id = qID;
    this.author = auth;
    this.quote = quot;
  }

}