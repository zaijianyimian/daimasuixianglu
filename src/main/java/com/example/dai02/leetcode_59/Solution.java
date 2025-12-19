package com.example.dai02.leetcode_59;
/**
 * 59. 螺旋矩阵 II
 */
public class Solution {
    public int[][] generateMatrix(int n) {
        int top = 0, bottom = n - 1, left = 0, right = n - 1;
        int[][] matrix = new int[n][n];
        int num = 1;
        while (num <= n * n) {
            for(int i = left;i <= right;i ++){
                matrix[top][i] = num ++;
            }
            top++;
            for(int i = top;i <= bottom;i ++){
                matrix[i][right] = num ++;
            }
            right--;
            for(int i = right;i >= left;i --){
                matrix[bottom][i] = num ++;
            }
            bottom--;
            for(int i = bottom;i >= top;i --){
                matrix[i][left] = num ++;
            }
            left++;
        }
        return matrix;
    }
}
