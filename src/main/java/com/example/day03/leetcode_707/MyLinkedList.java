package com.example.day03.leetcode_707;


import com.example.day03.leetcode_203.ListNode;

class MyLinkedList {
    int size;
    ListNode1 head;
    public MyLinkedList() {
        size = 0;
        head = new ListNode1(0);
    }
    
    public int get(int index) {
      if(index < 0 || index >= size){
          return -1;
      }
      ListNode1 cur = head;
      for(int i = 0;i < index + 1;i ++){
          cur = cur.next;
      }
      return cur.val;
    }
    
    public void addAtHead(int val) {
        addAtIndex(0,val);
    }
    
    public void addAtTail(int val) {
        addAtIndex(size,val);
    }
    
    public void addAtIndex(int index, int val) {
        if(index > size){
            return;
        }
        index = Math.max(0,index);
        size++;
        ListNode1 pre = head;
        for(int i = 0;i < index;i ++){
            pre = pre.next;
        }
        ListNode1 toAdd = new ListNode1(val);
        toAdd.next = pre.next;
        pre.next = toAdd;
    }
    
    public void deleteAtIndex(int index) {
        if(index < 0 || index >= size){
            return;
        }
        size--;
        ListNode1 pre = head;
        for(int i = 0;i < index;i ++){
            pre = pre.next;
        }
        pre.next = pre.next.next;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
class ListNode1{
    int val;
    ListNode1 next;
    public ListNode1(int val) {
        this.val = val;
        this.next = null;
    }
}
