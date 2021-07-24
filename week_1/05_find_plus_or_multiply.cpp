#include <iostream>
using namespace std;

int find_max_plus_or_multiply(int* arr,int len) {
	int multiply_sum = 0;
	//매개변수인 arr를 하나씩 순회
	for (int i = 0; i < len; i++) {
		if (arr[i] <= 1 or multiply_sum <= 1) // 현재 원소, 합이 1이하 일 경우
			multiply_sum += arr[i];
		else // 그 외
			multiply_sum *= arr[i];
	}
	return multiply_sum;
}

int main(void) {
	int array[] = { 0, 3, 5, 6, 1, 2, 4 };
	cout << find_max_plus_or_multiply(array, sizeof(array) / sizeof(int)) << '\n';
	return 0;
}
