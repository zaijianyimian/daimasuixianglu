package com.example.day12.leetcode_144;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(TreeNode head) {
        List<Integer> list = new ArrayList<>();
        if(head == null) return list ;
        
        preorder(list,head);
        return list;
    }
    private void preorder(List<Integer> list,TreeNode head){
        if(head == null){
            return;
        }
        list.add(head.val);
        preorder(list,head.left);
        preorder(list,head.right);
    }
}