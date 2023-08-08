import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        // 배열 오름차순 정렬
        Arrays.sort(array);
        int answer = array[array.length / 2];
        return answer;
    }
}