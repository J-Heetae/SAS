import java.util.*;

public class Solution {

    public int solution(int n) {
        int power = 0;
        while(n > 0) {
            if(n % 2 > 0) {
                n--;
                power++;
            }
            n /= 2;
        }
        return power;
    }
}