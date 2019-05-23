export class Output {
  
  // So all I've done is create the Words and Quotes classes,
  // and this Output class, that'll contain the word and it's frequency.

  word: string;
  frequency: number;

  constructor(wrd: string, freq: number) {
    this.word = wrd;
    this.frequency = freq;
  }

}