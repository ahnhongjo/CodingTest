package Level2;

import java.util.ArrayList;

public class orderSearch {
	public int[] solution(String[] info, String[] query) {
		
		ArrayList<person> people = new ArrayList<>();
		
		for(String inform:info) {
			String[] personInfo=inform.split(" ");
			
			person new1=new person(personInfo[0],personInfo[1],personInfo[2],personInfo[3],Integer.parseInt(personInfo[4]));
			people.add(new1);	
		}
		ArrayList<Integer> answer= new ArrayList<>();
		
		for(String qr:query) {
			String[] qrSplit=qr.split(" and ");
			String[] foodScore=qrSplit[3].split(" ");
			
			int num=0;
			for(person A:people) {
				
				if(!qrSplit[0].equals("-")&&!(qrSplit[0].equals(A.getLang()))) {
					continue;
				}
				if(!qrSplit[1].equals("-")&&!(qrSplit[1].equals(A.getBf())))
					continue;
				if(!qrSplit[2].equals("-")&&!(qrSplit[2].equals(A.getJs())))
					continue;
				if(!foodScore[0].equals("-")&&!(foodScore[0].equals(A.getFood())))
					continue;
				if(Integer.parseInt(foodScore[1])>A.getScore())
					continue;
				num++;
			}
			
			answer.add(num);
		}
        
		int[] arrayAnswer=new int[answer.size()];
		
		for(int i=0;i<answer.size();i++) {
			arrayAnswer[i]=answer.get(i);
		}
		
		return arrayAnswer;
        
    }
}

class person{
	String lang;
	String bf;
	String js;
	String food;
	int score;
	
	
	public person(String lang, String bf, String js, String food, int score) {
		super();
		this.lang = lang;
		this.bf = bf;
		this.js = js;
		this.food = food;
		this.score = score;
	}
	
	
	public String getLang() {
		return lang;
	}
	public void setLang(String lang) {
		this.lang = lang;
	}
	public String getBf() {
		return bf;
	}
	public void setBf(String bf) {
		this.bf = bf;
	}
	public String getJs() {
		return js;
	}
	public void setJs(String js) {
		this.js = js;
	}
	public String getFood() {
		return food;
	}
	public void setFood(String food) {
		this.food = food;
	}
	public int getScore() {
		return score;
	}
	public void setScore(int score) {
		this.score = score;
	}
	
	
}
