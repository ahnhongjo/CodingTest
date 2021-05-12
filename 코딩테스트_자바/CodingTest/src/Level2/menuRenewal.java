package Level2;

import java.util.*;



public class menuRenewal {
	static int a=4;
	
	static List<boolean[]> testtest = new ArrayList<boolean[]>();
	public String[] solution(String[] orders, int[] course) {
        String[] answer = {"a","b"};
        System.out.println(Arrays.toString(orders));
        System.out.println(Arrays.toString(course));
        
        for(int num:course) {
        	String[] tmp=numMenu(orders, num);
        	
        	List<String> premenu=new ArrayList<String>();
        	
        }
       
        int n = 4;
        int[] arr = {1, 2, 3, 4};
        boolean[] visited = new boolean[5];
        comb2(visited,0,5,2);
        System.out.println("Ãâ·Â");
        
        for (boolean[] prt :testtest) {
        	System.out.println(Arrays.toString(prt));
        }
       
        return answer;
    }
	
	public String[] numMenu(String[] orders, int num) {
		List<String> res= new ArrayList<String>();
		
		for(String menu: orders) {
			if (menu.length()>=num) {
				res.add(menu);
			}
		}
		
		return res.toArray(new String[res.size()]);
	}
	
	static void comb2(boolean[] visited, int depth, int n, int r) {
	    if (r == 0) {
	    	testtest.add(visited);
	    	System.out.println(Arrays.toString(visited));
	    	
	        return ;
	    }

	    if (depth == n) {
	        return;
	    }

	    visited[depth] = true;
	    comb2(visited, depth + 1, n, r - 1);

	    visited[depth] = false;
	    comb2(visited, depth + 1, n, r);
	}
	
	
	String getMenu(String sample, boolean[] arr) {
		String[] sampleArray=sample.split("");
		
		String result="";
		int n=0;
		for(boolean ar:arr) {
			if(ar) {
				result=result+sampleArray[n];
			}
			
			n++;
		}		
		return result;
	}
}
