#include <stdio.h>
#define MAX_SIZE 100 

typedef struct 
{
    int data[MAX_SIZE];
    int top;
} Stack;

int Empty(Stack *p) 
{
    return p->top == 0;
}

// Function to push an element 
void push(Stack *p, int n) 
{
    if (p->top == MAX_SIZE) 
    {
        printf("Error: Stack overflow\n");
        return;
    }
    p->data[p->top++] = n;
}

// Function to pop an element
int pop(Stack *p)
{
    if (Empty(p))
    {
        printf("Error: Stack underflow\n");
        return -1;
    }
    return p->data[--p->top];
}

int main() 
{
    Stack p;
    p.top = 0; 
    push(&p, 19);
    push(&p, 23);
    push(&p, 11);
    printf("element Popped: %d\n", pop(&p)); 
    printf("element Popped: %d\n", pop(&p)); 
    printf("element Popped: %d\n", pop(&p)); 
    printf("element Popped: %d\n", pop(&p)); 
    return 0;
}

""" output: 
element Popped: 11
element Popped: 23
element Popped: 19
Error: Stack underflow
element Popped: -1
"""
