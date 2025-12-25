package com.example.day09.kama_55;

import java.util.Scanner;

public class Main {
    public String changePlace(String str,int n){
        int r = str.length()-1;
        for(int i = 0;i < n - 1;i++){
            r --;
        }
        String append = str.substring(r,str.length());
        String sub = str.substring(0,r);
        return append + sub;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String str = sc.next();
        String res = new Main().changePlace(str,n);
        System.out.println(res);
    }
}
