class Solution {
    public int solution(int n) {
        // int answer = 0;
        
        // if (n % 7 == 0) {
        //     answer = n / 7;
        // } else {
        //     answer = n / 7 + 1;
        // }
        
        // 삼항연산자
        int answer = (n % 7 == 0) ? n/7 : n/7+1;
        
        return answer;
    }
}