class Solution {
    public int[] solution(int[] numbers) {
        // answer 배열 초기화. numbers 배열의 크기만큼
        int[] answer = new int[numbers.length];
        
        for (int i=0; i<numbers.length; i++) {
            answer[i] = numbers[i] * 2;
        }
        return answer;
    }
}