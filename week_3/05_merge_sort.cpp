#include<iostream>
using namespace std;

int arr[] = { 5, 3, 2, 1, 10, 6, 8, 7, 4,9};
int arr_size = sizeof(arr) / sizeof(arr[0]);
int* tmp;

void merge(int* arr, int left, int right) {
	int mid = (left + right)/2;
	int i = left;
	int j = mid + 1;
	int k = left;

	while (i<=mid && j<=right) {
		if (arr[i] <= arr[j])
			tmp[k++] = arr[i++];
		else
			tmp[k++] = arr[j++];
	}

	int tmp_idx = i > mid ? j : i;

	while (k<=right) {
		tmp[k++] = arr[tmp_idx++];
	}

	for (int i = left; i <= right; i++) 
		arr[i] = tmp[i];
	
}

void merge_sort(int* arr,int left,int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		merge_sort(arr, left, mid);
		merge_sort(arr, mid + 1, right);
		merge(arr, left, right);
	}
}

int main(void) {
	for (int i = 0; i < arr_size; i++) {
		cout << arr[i] << ' ';
	}
	cout << '\n';
	tmp = new int[arr_size];
	merge_sort(arr,0,arr_size-1);

	for (int i = 0; i < arr_size; i++) {
		cout << arr[i] << ' ';
	}
	cout << '\n';

	return 0;
}