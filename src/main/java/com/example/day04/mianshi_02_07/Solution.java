package com.example.day04.mianshi_02_07;

import com.example.day04.leetcode_24.ListNode;

public class Solution {
    public ListNode getIntersectionNode(ListNode headA,ListNode headB){
        ListNode curA = headA;
        ListNode curB = headB;
        int lenA = 0,lenB = 0;
        while(curA != null){
            lenA ++;
            curA = curA.next;
        }

        while(curB != null){
            lenB ++;
            curB = curB.next;
        }

        curA = headA;
        curB = headB;
        if(lenB > lenA){
            int tmp = lenA;
            lenA = lenB;
            lenB = tmp;
            ListNode tmpNode = curA;
            curA = curB;
            curB = tmpNode;
        }

        int gap = lenA - lenB;
        while(gap > 0){
            curA = curA.next;
            gap --;
        }

        while(curA != null){
            if(curA == curB){
                return curA;
            }
            curA = curA.next;
            curB = curB.next;
        }
        return null;
    }
}
