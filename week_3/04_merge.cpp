#include<iostream>
#include<vector>
using namespace std;

int array1[5] = { 1,2,3,4,5 };
int array2[5] = { 6,7,8,9,10 };
int arr_size = sizeof(array1) / sizeof(int);
vector<int> merge_arr;

void merge(int* array1, int* array2) {
	int arr1_idx = 0;
	int arr2_idx = 0;
	while (arr1_idx < arr_size && arr2_idx < arr_size) {
		if (array1[arr1_idx] < array2[arr2_idx]) {
			merge_arr.push_back(array1[arr1_idx]);
			arr1_idx++;
		}
		else {
			merge_arr.push_back(array2[arr2_idx]);
			arr2_idx++;
		}
	}
	if (arr1_idx == arr_size) {
		while (arr2_idx < arr_size) {
			merge_arr.push_back(array2[arr2_idx]);
			arr2_idx++;
		}
	}
	if (arr2_idx == arr_size) {
		while (arr1_idx < arr_size) {
			merge_arr.push_back(array1[arr1_idx]);
			arr1_idx++;
		}
	}
}

int main(void) {
	for (int i = 0; i < arr_size; i++) {
		cout << array1[i] << ' ';
	}
	cout << '\n';

	for (int j = 0; j < arr_size; j++) {
		cout << array2[j] << ' ';
	}
	cout << '\n';

	merge(array1,array2);

	for (int i = 0; i < (arr_size * 2); i++) {
		cout << merge_arr[i] << ' ';
	}
	cout << '\n';

	return 0;
}