#include <stdio.h>
#define MAX_SIZE 100 

typedef struct 
{
    int data[MAX_SIZE];
    int head;
    int tail;
    int length;
} Queue;

void initQueue(Queue *queue) 
{
    queue->head = 0;
    queue->tail = 0;
    queue->length = 0;
}

int Empty(Queue *queue) 
{
    return queue->length == 0;
}

// Function to check if the queue is full
int Full(Queue *queue) 
{
    return queue->length == MAX_SIZE;
}

// Function to enqueue 
void enqueue(Queue *queue, int q) 
{
    if (Full(queue)) 
    {
        printf("Error: Queue overflow\n");
        return;
    }
    queue->data[queue->tail++] = q;
    queue->length++;
    if (queue->tail == MAX_SIZE)
        queue->tail = 0; 
}

// Function to dequeue 
int dequeue(Queue *queue) 
{
    if (Empty(queue))
    {
        printf("Error: Queue underflow\n");
        return -1; 
    }
    int q = queue->data[queue->head++];
    queue->length--;
    if (queue->head == MAX_SIZE)
        queue->head = 0; 
    return q;
}

int main() 
{
    Queue queue;
    initQueue(&queue); 
    enqueue(&queue, 23);
    enqueue(&queue, 35);
    enqueue(&queue, 12);

    printf("element Dequeued: %d\n", dequeue(&queue)); 
    printf("element Dequeued: %d\n", dequeue(&queue)); 
    printf("element Dequeued: %d\n", dequeue(&queue)); 
    printf("element Dequeued: %d\n", dequeue(&queue)); 

    return 0;
}

"""
element Dequeued: 23
element Dequeued: 35
element Dequeued: 12
Error: Queue underflow
element Dequeued: -1
"""
