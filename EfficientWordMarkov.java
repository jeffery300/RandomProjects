import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

public class EfficientWordMarkov implements MarkovInterface<WordGram> {
	private String myText;
	private Random myRandom;
	private int myOrder;
	HashMap<WordGram, ArrayList<String>> map = new HashMap<WordGram,ArrayList<String>>();
	private static String PSEUDO_EOS = "";
	private static int RANDOM_SEED = 1234;
	
	public EfficientWordMarkov(int order) {
		myRandom = new Random(RANDOM_SEED);
		myOrder = order;
	}
	
//	public EfficientWordMarkov() {
//		this(3);
//	}
	//use wordgram as keys rather than strings, store whole words rather than indivudal letters
	public void setTraining(String text) {
		myText = text;
		String[] txtarray = text.split("\\s+");
		int stop = txtarray.length-myOrder; 
		for(int i = 0; i<stop; i++)
		{
			WordGram ngram = new WordGram(txtarray,i,myOrder);
			if(!map.containsKey(ngram))
			{
				map.put(ngram, new ArrayList<String>());
			}
			ArrayList<String> alreadyin = map.get(ngram);
			alreadyin.add(txtarray[i+myOrder]);
			//alreadyin.add(text.substring(i+myOrder,i+myOrder+1));
			map.put(ngram, alreadyin);	
		}
		
	}
	public int size() {
		return myText.length();
	}
	
    //use wordgram rather than string, create a wordgram instead of calling substring
	//rather than concatenating strings, call shiftAdd() to create a new wordGram
	public String getRandomText(int length) {
		StringBuilder sb = new StringBuilder();
		String [] textarray = myText.split("\\s+");
		int index = myRandom.nextInt(textarray.length - myOrder);
		
		//String current = myText.substring(index, index + myOrder);
		WordGram current = new WordGram(textarray,index,myOrder);
		//System.out.printf("first random %d for '%s'\n",index,current);
		sb.append(current);
		for(int k=0; k < length-myOrder; k++){
			ArrayList<String> follows = getFollows(current);
			if (follows.size() == 0){
				break;
			}
			index = myRandom.nextInt(follows.size());
			
			String nextItem = follows.get(index);
			if (nextItem.equals(PSEUDO_EOS)) {
				//System.out.println("PSEUDO");
				break;
			}
			sb.append(" "+ nextItem);
			//current = current.substring(1)+ nextItem;
			current = current.shiftAdd(nextItem);
		}
		return sb.toString();
	}
	
	public ArrayList<String> getFollows(WordGram key){
		return map.get(key);

	}

	@Override
	public int getOrder() {
		return myOrder;
	}

}
