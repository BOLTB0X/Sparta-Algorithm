#include <stdio.h>

void swap(int* a, int* b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void selection_sort(int* array[], int n) {
	for (int i = 0; i < n; i++) {
		int min_idx = i;
		for (int j = i; j < n; j++) {
			if (array[min_idx] > array[j])
				min_idx = j;
		}
		swap(&array[i], &array[min_idx]);
	}
}

int main(void) {
	int array[5] = { 4,6,1,2,0 };
	int len = sizeof(array) / sizeof(int);

	for (int i = 0; i < len; i++) 
		printf("%d ", array[i]);
	printf("\n");

	selection_sort(array, len);

	for (int i = 0; i < len; i++) 
		printf("%d ", array[i]);
	printf("\n");

	return 0;
}