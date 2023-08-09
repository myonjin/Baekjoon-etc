import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder str = new StringBuilder();

        // a, b, c, d, e, f
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        int f = Integer.parseInt(st.nextToken());

        int aswX = 0;
        int aswY = 0;

        loop:
        for(int x = -999; x < 1000; x++)
            for(int y = -999; y < 1000; y++)
                if((a*x+b*y==c)&&(d*x+e*y==f)){
                    aswX = x;
                    aswY = y;
                    break loop;
                }

        str.append(aswX + " " + aswY);

        System.out.print(str);
        br.close();
    }
}