package Level3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class jewelShopping {
	public int[] solution(String[] gems) {
        int[] answer = {};
        
        System.out.println(Arrays.toString(gems));
        
        ArrayList<String> gemKind = new ArrayList<>();
        
        for(String g:gems) {
        	if(!gemKind.contains(g)) {
        		gemKind.add(g);
        	}
        }
        
        System.out.println(gemKind);
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String g:gemKind) {
        	map.put(g, 0);
        }
        
        int min=gems.length+1;
        ArrayList<String> window=new ArrayList<>();
        int start=0;
        int end=0;
        int[] startEnd = {0,0};
        
        while(end!=gems.length) {
    		window.add(gems[end]);
    		map.put(gems[end], map.get(gems[end])+1);
    		
    		
        	if(allJewel(map)) {
        		while(map.get(gems[start])>1) {
        			map.put(gems[start], map.get(gems[start])-1);
        			start++;
        			window.remove(0);
        		}
        		
        		if(min>end-start+1) {
        			min=start-end+1;
        			startEnd[0]=start;
        			startEnd[1]=end;
        		}
        	}
        	
        	System.out.println(window);
        	System.out.println(Arrays.toString(startEnd));
        	end++;
        }
        startEnd[0]+=1;
        startEnd[1]+=1;
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
