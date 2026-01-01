package com.example.day14.leetcode_513;

import com.example.day13.leetcode_226.TreeNode;

class Solution {
    int maxDepth = Integer.MIN_VALUE;
    int result = 0;

    public int findBottomLeftValue(TreeNode root) {
        result = root.val;
        traverse(root, 0);
        return result;
    }

    public void traverse(TreeNode root, int depth) {
        if (root == null) return;
        if (root.left == null && root.right == null) {
            if (depth > maxDepth) {
                maxDepth = depth;
                result = root.val;
                return;
            }
        }
        if (root.left != null) {
            traverse(root.left, depth + 1);
        }
        if (root.right != null) {
            traverse(root.right, depth + 1);
        }
    }
}
