import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> queue = new LinkedList<>();
        for(int i=0; i<priorities.length; i++) {
            queue.offer(new int[]{i, priorities[i]});
        }
        
        Arrays.sort(priorities);
        
        int order = 1;
        int priorIdx = priorities.length - 1;
        while(!queue.isEmpty()) {
            int[] poll = queue.poll();
            if(poll[1] == priorities[priorIdx]) {
                if(poll[0] == location) {
                    break;
                }
                priorIdx--;
                order++;
            } else {
                queue.offer(poll);
            }
        }
        return order;
    }
}