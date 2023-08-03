import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int[] arr = new int[366];
        int ans = 0;
        int max_row = 0;
        int col = 0;
        for (int i = 0; i<T; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            // 시작 지점 , 도착 지점 1씩 더해주기
            for (int j = s; j<=e; j++){
                arr[j] +=1;
            }
        }
        for (int i=0; i<366; i++){
            if (arr[i] >=1 ){
                col++;
                if (arr[i] > max_row) {
                    max_row = arr[i];

                }
            } else{
                ans += max_row*col;
                max_row=0;
                col=0;
            }
        }
        ans += max_row*col;
        System.out.println(ans);
        
        // 여기에 코드를 작성해주세요.
    }
}


