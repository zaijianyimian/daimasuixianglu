package com.example.day13.leetcode_111;

import com.example.day13.leetcode_226.TreeNode;

public class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftDepth = minDepth(root.left);
        int rightDepth = minDepth(root.right);
        if(leftDepth == 0) return rightDepth + 1;
        if(rightDepth == 0)return leftDepth + 1;
        return Math.min(leftDepth,rightDepth) + 1;
    }
}
