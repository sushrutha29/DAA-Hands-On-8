#include <stdio.h>
#include <stdlib.h>

typedef struct quad 
{
    int key;
    struct quad *next;
} quad;

typedef struct 
{
    quad *head;
    quad *nil;
} List;

void initList(List *list) 
{
    list->head = NULL;
    list->nil = (quad *)malloc(sizeof(quad));
    list->nil->next = NULL;
}


quad *listSearch(List *list, int k) 
{
    quad *x = list->head;
    while (x != list->nil && x->key != k) 
    {
        x = x->next;
    }
    return x;
}

void listDelete(List *list, quad *x) 
{
    quad *prev = NULL;
    quad *current = list->head;

    while (current != NULL && current != x)
    {
        prev = current;
        current = current->next;
    }

    if (prev == NULL) 
    {
        list->head = x->next;
    } else {
        prev->next = x->next;
    }

    free(x);
}

quad *listSearch0(List *list, int k)
{
    quad *x = list->nil->next;
    while (x != list->nil && x->key != k) 
    {
        x = x->next;
    }
    return x;
}

void listInsert0(List *list, int x) 
{
    quad *node = (quad *)malloc(sizeof(quad));
    node->key = x;
    node->next = list->nil->next;
    list->nil->next = node;
}

void listDelete0(List *list, quad *x)
{
    quad *prev = NULL;
    quad *current = list->nil->next;

    while (current != NULL && current != x) 
    {
        prev = current;
        current = current->next;
    }

    if (prev == NULL) 
    {
        list->nil->next = x->next;
    } else 
    {
        prev->next = x->next;
    }

    free(x);
}

int main()
{
    List list;
    initList(&list); 
    listInsert0(&list, 33);
    listInsert0(&list, 42);
    listInsert0(&list, 17);

    if (listSearch0(&list, 17) != NULL)
    {
        printf("Detected: 17\n");
    } else 
    {
        printf("Not Detected\n");
    }

    listDelete0(&list, listSearch0(&list, 45));
    if (listSearch0(&list, 45) != NULL)
    {
        printf("Detected: 45\n");
    } else
    {
        printf("Not Detected: 45\n");
    }

    return 0;
}

"""
output: 
Detected: 17
Not Detected: 21
"""
