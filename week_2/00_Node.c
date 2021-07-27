#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int data;
	struct Node* next; // 이 구조체 자체를 가리키는 포인터이므로 struct으로 선언
} Node;

Node* head; //노드 머리 선언

void main(void) {
	head = (Node*)malloc(sizeof(Node)); //헤드 선언
	Node* node1 = (Node*)malloc(sizeof(Node));
	node1->data = 1;
	Node* node2 = (Node*)malloc(sizeof(Node));
	node2->data = 2;
	Node* node3 = (Node*)malloc(sizeof(Node));
	node3->data = 3;

	head->next = node1; //노드1를 머리로
	node1->next = node2;
	node2->next = node3;
	node3->next = NULL;

	Node* cur = head->next;
	while (cur != NULL) {
		printf("%d ", cur->data);
		cur = cur->next; //한칸씩 넘어간다
	}
}