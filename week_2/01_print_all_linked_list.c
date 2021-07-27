#include <stdio.h>
#include <stdlib.h>

typedef struct { //���� ����Ʈ
	int data; //data�� ������ �ɹ�
	struct Node* next; //���� ����� �ּҸ� ������ ������
} Node;

Node* head; //���� ���


//�ڿ� �߰�
void append(Node* root,int data) {
	if (root->next == NULL) {
		// ����Ʈ�� ������ NULL �̸� (����Ʈ�� ���������) 
		// NULL�� �ڽ��� �ּҷ� �ٲ�
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

// �տ��� �߰� 
void appendleft(Node* root, int data) {
	Node* new_node = (Node*)malloc(sizeof(Node));
	new_node->data = data; //���ο� ����� �����͸� �Է�
	//���ο� ��带 �����ϸ� ����� next (���� ��� �ּ�)�� ����
	new_node->next = root->next; 
	//������� next�� ���ο� ����� �ּҷ� �ٲ�
	root->next = new_node;
}

//��ü ���
void print_all(Node *root) {
	Node* cur = root->next;
	while (cur != NULL) {
		printf("%d ", cur->data);
		cur = cur->next;
	}
	printf("\n");
}

void main(void) {
	head = (Node*)malloc(sizeof(Node)); //�Ӹ� ��� ����
	head->next = NULL;

	append(head, 2);
	append(head, 3);
	append(head, 4);
	appendleft(head, 1);

	print_all(head);
}
