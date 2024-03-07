class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* fst = head;
        ListNode* slw = head;
        if(head==NULL) return NULL;
        
        else{
        while(fst!=NULL and fst->next!=NULL)
        {
            fst=fst->next->next;
             slw=slw->next;
        }
           
            return slw;
    }
    }
};