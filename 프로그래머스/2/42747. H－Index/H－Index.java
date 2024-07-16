import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int h = 0;
        int N = citations.length;
        Integer[] arr = Arrays.stream(citations).boxed().toArray(Integer[]::new);
        Arrays.sort(arr, Collections.reverseOrder());
        for (int i = 0 ; i<N; i++){
            if(i>= arr[i]){
                return i;
            }
        }
        return N;
    }
}


// def solution(citations):
//     answer = 0
//     h = 0
//     N = len(citations)
//     citations.sort(reverse = True)
//     for idx,c in enumerate(citations):
//         if idx >= c:
//             return idx
    
//     return N