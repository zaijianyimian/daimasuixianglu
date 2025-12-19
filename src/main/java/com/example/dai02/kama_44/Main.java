package com.example.dai02.kama_44;

import java.util.Scanner;

/**
 * 开发商购买土地
 */
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int sum = 0;

        int[][] arr = new int[n][m];
        for(int i = 0;i < n;i ++){
            for(int j = 0;j < m;j ++){
                arr[i][j] = sc.nextInt();
                sum += arr[i][j];
            }
        }
        int[] hang = new int[n];
        for(int i = 0;i < n;i ++){
            for(int j = 0;j < m;j ++){
                hang[i] += arr[i][j];
            }
        }
        int[] lie = new int[m];
        for(int j = 0;j < m;j ++){
            for(int i = 0;i < n;i ++){
                lie[j] += arr[i][j];
            }
        }
        int res = Integer.MAX_VALUE;
        int pre = 0;
        for(int i = 0;i < n;i ++){
            pre += hang[i];
            res = Math.min(res,Math.abs((sum - pre) -  pre));
        }
        pre = 0;
        for(int j = 0;j < m;j ++){
            pre += lie[j];
            res = Math.min(res,Math.abs((sum - pre) - pre));
        }
        System.out.println(res);
    }
}
