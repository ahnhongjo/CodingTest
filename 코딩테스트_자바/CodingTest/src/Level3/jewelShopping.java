package Level3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class jewelShopping {
	public int[] solution(String[] gems) {
        int[] answer = {};
        
        ArrayList<String> gemKind = new ArrayList<>();
        
        for(String g:gems) {
        	if(!gemKind.contains(g)) {
        		gemKind.add(g);
        	}
        }
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String g:gemKind) {
        	map.put(g, 0);
        }
        
        int min=gems.length+1;
        int start=0;
        int end=0;
        int[] startEnd = {0,0};
        
        while(end!=gems.length) {
    		map.put(gems[end], map.get(gems[end])+1);
        	if(allJewel(map)) {
        		while(map.get(gems[start])>1) {
        			map.put(gems[start], map.get(gems[start])-1);
        			start++;
        		}
        		
        		if(min>end-start+1) {
        			min=end-start+1;
        			startEnd[0]=start;
        			startEnd[1]=end;
        		}
        	}
        	end++;
        }
        startEnd[0]+=1;
        startEnd[1]+=1;
        System.out.println(Arrays.toString(startEnd));
        return startEnd;
    }
	
	boolean allJewel(HashMap<String,Integer> h) {
		
		for(int j:h.values()) {
			if(j==0)
				return false;
		}
		
		return true;
	}
}
