import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        PriorityQueue<int[]> heap = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        int currentTime = 0;
        int num = jobs.length;
        Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]);
        int k = 0;
        int index = 0;
        while (k < num){
            while (index < num && jobs[index][0] <= currentTime){
                heap.add(jobs[index++]);
            }
            
            if (!heap.isEmpty()){
                int[] currentJob = heap.poll();
                currentTime += currentJob[1];
                answer += currentTime - currentJob[0];
                k++;
            } else{
                currentTime++;
            }
        } 
        return answer/num;
    }
}