#include <stdio.h>

void swap(int* a, int* b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void insertion_sort(int* arr[], int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (arr[i - j - 1] > arr[i - j]) {
				swap(&arr[i - j - 1], &arr[i - j]);
			}
			else {
				break;
			}
		}
	}
}

int main(void) {
	int arr[5] = { 2,4,3,5,1 };
	int len = sizeof(arr) / sizeof(int);

	for (int i = 0; i < len; i++)
		printf("%d ", arr[i]);
	printf("\n");

	insertion_sort(arr, len);

	for (int i = 0; i < len; i++)
		printf("%d ", arr[i]);
	printf("\n");

	return 0;
}