package com.example.day04.leetcode_19;

import com.example.day04.leetcode_24.ListNode;

public class Solution {
    public ListNode removeNthFromEnd(ListNode head,int n){
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int ind = 0;
        ListNode p = head;
        while(p != null){
            ind++;
            p = p.next;
        }
        ind = ind - n;
        p = dummy;
        while(ind > 0){
            p = p.next;
            ind--;
        }
        p.next = p.next.next;
        return dummy.next;
    }
}
