package com.example.day12.leetcode_144;


import java.util.ArrayList;
import java.util.List;




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