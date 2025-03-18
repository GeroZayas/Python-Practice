#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

typedef struct {
	int items[MAX_VERTICES];
	int front;
	int rear;
} Queue;

void enqueue(Queue* q, int value) {
	q->items[++q->rear] = value;
