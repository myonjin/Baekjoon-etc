import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        for (char chr : a.toCharArray()) {
            if (Character.isUpperCase(chr)) {
                System.out.print(Character.toLowerCase(chr));
            }
            else {
                System.out.print(Character.toUpperCase(chr));
            }
        }
    }
}
