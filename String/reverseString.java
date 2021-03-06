import java.util.*;

public class reverseString{
	public static void main(String args[]){
		String s="helloworld";
		String result=reverse_stringC(s);
		System.out.println(result);
	}


	public static String reverse_stringA(String s) {
        StringBuilder sb = new StringBuilder(s);
        return sb.reverse().toString();
    }

    //method 2: use swap method
    public static String reverse_stringB(String s){
        if(s == null || s.length() == 0)
            return "";
        char[] cs = s.toCharArray();
        int begin = 0, end = s.length() - 1;
        while(begin <= end){
            char c = cs[begin];
            cs[begin] = cs[end];
            cs[end] = c;
            begin++;
            end--;
        }
        
        return new String(cs);
    }

    //method 3: traverse the string from end to front
    public static String reverse_stringC(String s){
        String result="";
        for(int i=s.length()-1;i>=0;i--){
            result+=s.charAt(i);
        }

        return result;
    }
}