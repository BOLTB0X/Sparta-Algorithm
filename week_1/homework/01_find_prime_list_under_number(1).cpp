#include <iostream>
#include <vector>
using namespace std;

vector<int> find_prime_list_under_number(int number) {
	vector<int> prime_list;
	for (int i = 2; i <= number; i++) {
		int cnt = 0;
		for (int j = 2; j <= i; j++) {
			if (i % j == 0)
				cnt++;
		}
		if (cnt == 1) //나눠지는 수가 1개
			prime_list.push_back(i);
	}
	return prime_list;
}

int main(void) {
	vector<int> result; 
	result= find_prime_list_under_number(20);

	for (int i = 0; i < result.size(); i++) {
		cout << result[i] << ' ';
	}
	return 0;
}