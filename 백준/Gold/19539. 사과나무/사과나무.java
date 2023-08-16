import java.sql.Array;
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int[] arr = new int[N];
        for (int i = 0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int sum_2 = 0;
        for (int ar: arr) sum_2+=ar/2;
        int arr_sum = Arrays.stream(arr).sum();
        if ( (arr_sum/3 <= sum_2) && (arr_sum%3) == 0){
            System.out.println("YES");
        } else{
            System.out.println("NO");
        }
        

    }
}