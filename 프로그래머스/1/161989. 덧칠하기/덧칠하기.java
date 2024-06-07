class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int temp = 0;
        for (int i=0 ; i<section.length; i++){
            // System.out.println(section[i]);
            if (temp < section[i]){
                temp = section[i] + m - 1;
                answer += 1;
            }
        }
        return answer;
    }
}