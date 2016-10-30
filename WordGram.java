//methods necessary:
//WordGram(String[], int, int)
//int hashCode()
//String toString()
//boolean equals(Object other)
//int compareTo(WordGram other)
//WordGram shiftAdd(String last) 

public class WordGram implements Comparable<WordGram> {
	  private String[] myWords;
	  private int myHash;
	  public WordGram(String[] source, int start, int size){
		  myWords = new String[size];
//		  for (int i = start; i<start+size; i++){
//			  myWords[i-start]=source[i];
//		  }
		  //easier one line way to make a copy of an array
		 System.arraycopy(source, start, myWords, 0, size);
	  }
	  public int length(){
		  return myWords.length;
	  }
	  public int hashCode(){
		  //must take indices of array into account somehow, done by multiplying 2 to the power of the index position
		  int hash = 0;
		  for(int k=0; k < myWords.length; k++) {
		      hash += myWords[k].hashCode()*Math.pow(2, k);
		  }
		  myHash = hash;
		  return hash;
	  }

	  public boolean equals(Object other){
		  if (! (other instanceof WordGram)) 
			  return false;
		  WordGram wg = (WordGram) other;
		  if(this.myWords.length != wg.myWords.length)
			  return false;
		  
		  for (int i = 0; i<this.myWords.length; i++)
		  {
			  if(!this.myWords[i].equals(wg.myWords[i]))
				  return false;
		  }
		  return true;
	  }
	  public int compareTo(WordGram other){
		  int length = 0;
		  int thislonger = 0;
		  if(this.myWords.length>other.myWords.length){
			  length = other.myWords.length;
			  thislonger = 1;
		  }
		  if(this.myWords.length<other.myWords.length){
			  length = this.myWords.length;
			  thislonger = -1;
		  }
		  if(this.myWords.length == other.myWords.length)
			  length = this.myWords.length;
		  for(int i = 0; i<length; i++)
		  {
			  if(!this.myWords[i].equals(other.myWords[i]))
				  return this.myWords[i].compareTo(other.myWords[i]);
		  }
		  if(thislonger == 1)
			  return 1;
		  if(thislonger == -1)
			  return -1;
		  return 0;
	  }
	  public WordGram shiftAdd(String last){
		  
		  for(int i = 0; i<myWords.length-1; i++){
			  	myWords[i] = myWords[i+1];
		  }
		  myWords[myWords.length-1] = last;
		  WordGram wg = new WordGram(this.myWords,0,this.myWords.length);
		  return wg;
	  }
	  public String toString(){
		  String answer = "{";
		  for(int i = 0; i<myWords.length; i++)
		  {
			 if(i != myWords.length-1)
				 answer += myWords[i] + ",";
			 else
				 answer += myWords[i];	 
		  }
		  answer += "}";
		  return answer;
	  }

}
