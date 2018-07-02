import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {



    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String a = scanner.nextLine();

        String b = scanner.nextLine();
        int common = commonCharacters(a,b);
        System.out.println((a.length()-common)+(b.length()-common));
        scanner.close();
    }

    public static int commonCharacters(String s1, String s2)
    {
        //return intersection a,b
        StringBuffer a = new StringBuffer(s1);
        StringBuffer b = new StringBuffer(s2);
        int counter = 0;
        for (int i=0;i<a.length();i++)
        {
            for(int j=0;j<b.length();j++)
            {
                if (s1.charAt(i)==b.charAt(j))
                {
                    counter++;
                    //a.deleteCharAt(i);
                    b.deleteCharAt(j);
                    break;
                }
            }
        }
        return counter;
        
    }
    
}
