#include <iostream>
using namespace std;

int arr[6] = { 3, 5, 6, 1, 2, 4 };

bool is_number_exist(int number, int* arr) {
	bool check=false;
	for (int i = 0; i < 6; i++) { //하나씩 비교
		if (arr[i] == number)
			return true;
	}
	return false;
}

int main(void) {
	cout << is_number_exist(9, arr) << endl;
	return 0;
}
