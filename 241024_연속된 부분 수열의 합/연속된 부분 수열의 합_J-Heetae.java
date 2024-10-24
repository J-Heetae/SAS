class Solution {
    public int[] solution(int[] seq, int k) { 
        int leftIdx = 0;
        int rightIdx = 0;
        int sum = seq[0];
        int length = 1;
        int minLength = Integer.MAX_VALUE;
        int[] answer = new int[2];
        while(leftIdx <= rightIdx && rightIdx < seq.length) {
            if(sum <= k) {
                if(sum == k && length < minLength) {
                    answer[0] = leftIdx;
                    answer[1] = rightIdx;
                    minLength = length;
                }
                rightIdx++;
                if(rightIdx == seq.length) {
                    break;
                }
                length++;
                sum += seq[rightIdx];
            } else {
                sum -= seq[leftIdx];
                leftIdx++;
                length--;
            }
        }
        return answer;
    }
}