package KakaoCommerce;

import java.util.ArrayList;

public class programming1 {
	public int solution(int[] gift_cards, int[] wants) {
        
		ArrayList<Integer>wantsList = new ArrayList<>();
		
		for(int want:wants) {
			wantsList.add(want);
		}
		
		for(int gift:gift_cards) {
			if(wantsList.contains(gift)) {
				wantsList.remove((Integer)gift);
			}
		}
		
		int answer=wantsList.size();
        return answer;
    }
}
