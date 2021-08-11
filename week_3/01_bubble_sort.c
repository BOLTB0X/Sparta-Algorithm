#include <stdio.h>
void swap(int* a, int* b) {
	int tmp;
	tmp = *a;
	*a = *b;
	*b = tmp;
}

void bubble_sort(int* array[], int len) {
	for (int i = 0; i < len-1; i++) {
		for (int j = 0; j < len - i-1; j++) {
			if (array[j] > array[j + 1]) {
				swap(&array[j], &array[j + 1]);
			}
		}
	}
}

int main(void) {
	int input_array[5] = { 4,6,2,9,1 };
	int len = sizeof(input_array) / sizeof(int);
	for (int i = 0; i < len; i++) {
		printf("%d ", input_array[i]);
	}
	printf("\n");
	
	bubble_sort(input_array,len);

	for (int i = 0; i <len; i++) {
		printf("%d ", input_array[i]);
	}
	printf("\n");
	return 0;
}