package com.example.day08.kama_54;

import java.util.Scanner;

public class Solution {
    private String replaceNumber(String s){
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(Character.isLowerCase(c)){
                sb.append(c);
            }else{
                sb.append("number");
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String res = new Solution().replaceNumber(s);
        System.out.println(res);
    }
}
