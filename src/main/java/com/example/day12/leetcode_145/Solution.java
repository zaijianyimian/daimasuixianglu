package com.example.day12.leetcode_145;


import com.example.day12.leetcode_144.TreeNode;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> postorderTraversal(TreeNode head) {
      List<Integer> list = new ArrayList<>();
        if(head == null) return list ;
        
        preorder(list,head);
        return list;
    }
    private void preorder(List<Integer> list,TreeNode head){
        if(head == null){
            return;
        }

        preorder(list,head.left);
        preorder(list,head.right);
        list.add(head.val);
    }
}