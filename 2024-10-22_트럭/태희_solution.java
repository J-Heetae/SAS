import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int w = sc.nextInt();
        int L = sc.nextInt();

        int[] truckWeight = new int[n];
        for(int i=0; i<n; i++) {
            truckWeight[i] = sc.nextInt();
        }

        Queue<int[]> q = new LinkedList<>();
        int truckIdx = 0;
        int onWeight = 0;
        int time = 0;
        for(; time<100000; time++) {
            if(truckIdx == n && q.isEmpty()) {
                break;
            }

            if(!q.isEmpty() && q.peek()[1] == time) { //빠져오는 시간이랑 일치
                int[] poll = q.poll();
                onWeight -= poll[0];
            }

            if(truckIdx < n && onWeight + truckWeight[truckIdx] <= L) {
                q.offer(new int[]{truckWeight[truckIdx], time + w});
                onWeight += truckWeight[truckIdx];
                truckIdx++;
            }
        }
        System.out.println(time);
    }
}
