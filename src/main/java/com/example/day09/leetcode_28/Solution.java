package com.example.day09.leetcode_28;

/**
 * 正常应该用kmp算法解决,这里取巧了
 */
public class Solution {
    public int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }
}