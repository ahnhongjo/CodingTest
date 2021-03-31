package Level2;

public class binChangeIter {
	
	public int[] solution(String s) {
        int num_0=0;
        int iter_num=0;
        while(true) {
        	if(s.equals("1")) {
        		int[] answer={iter_num,num_0};
        		return answer;
        	}
        	int num=0;
        	for(int i=0;i<s.length();i++) {
        		if(s.charAt(i)=='1') {
        			num++;
        			
        		}
        		else {
        			num_0++;
        		}
        	}
        	s=Integer.toBinaryString(num);
        	iter_num++;
        }
    }
	
	
}
