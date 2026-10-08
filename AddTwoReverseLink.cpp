#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node* next;

    Node(int val)
    {
        data = val;
        next = nullptr;
    }
};

Node* addTwoNumbers(Node* l1, Node* l2)
{
    Node* dummy = new Node(0);
    Node* current = dummy;

    int carry = 0;

    while(l1 != nullptr || l2 != nullptr || carry != 0)
    {
        int digit1 = 0;
        int digit2 = 0;

        if(l1 != nullptr)
        {
            digit1 = l1->data;
        }

        if(l2 != nullptr)
        {
            digit2 = l2->data;
        }

        int sum = digit1 + digit2 + carry;

        int digit = sum % 10;

        carry = sum / 10;

        current->next = new Node(digit);

        current = current->next;

        if(l1 != nullptr)
        {
            l1 = l1->next;
        }

        if(l2 != nullptr)
        {
            l2 = l2->next;
        }
    }

    return dummy->next;
}