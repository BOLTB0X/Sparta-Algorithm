#include <iostream>
using namespace std;
int arr[5] = {3,5,1,2,4};

int find_max_num(int* arr) {
	int max_value=arr[0];
	for (int i = 1; i < 5; i++) {
		if (max_value < arr[i]) max_value=arr[i];
	}

	return max_value;
}

int main(void) {
	cout << find_max_num(arr);
}