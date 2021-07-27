#include <stdio.h>
#include <stdlib.h>

typedef struct { //연결 리스트
	int data; //data를 저장할 맴버
	struct Node* next; //다음 노드의 주소를 저장할 포인터
} Node;

Node* head; //시작 노드


//뒤에 추가
void append(Node* root,int data) {
	if (root->next == NULL) {
		// 리스트의 다음이 NULL 이면 (리스트가 비어있으면) 
		// NULL을 자신의 주소로 바꿈
		Node* new_node = malloc(sizeof(Node));
		new_node->data = data;
		new_node->next = NULL;

		root->next = new_node;
	}
	else {
		Node* cur = root;
		//traverse
		while (cur->next != NULL) {
			cur = cur->next;
		}
		Node* new_node = malloc(sizeof(Node));
		new_node->data = data;
		new_node->next = NULL;

		cur->next = new_node;
	}
}

// 앞에다 추가 
void appendleft(Node* root, int data) {
	Node* new_node = (Node*)malloc(sizeof(Node));
	new_node->data = data; //새로운 노드의 데이터를 입력
	//새로운 노드를 생성하면 헤드의 next (다음 노드 주소)를 대입
	new_node->next = root->next; 
	//헤드노드의 next를 새로운 노드의 주소로 바꿈
	root->next = new_node;
}

//전체 출력
void print_all(Node *root) {
	Node* cur = root->next;
	while (cur != NULL) {
		printf("%d ", cur->data);
		cur = cur->next;
	}
	printf("\n");
}

void main(void) {
	head = (Node*)malloc(sizeof(Node)); //머리 노드 생성
	head->next = NULL;

	append(head, 2);
	append(head, 3);
	append(head, 4);
	appendleft(head, 1);

	print_all(head);
}
