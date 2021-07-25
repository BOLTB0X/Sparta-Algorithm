#include <iostream>
using namespace std;

//에라토스테네스의 체
int prime_list[10000];
void find_prime_list_under_number(int number) {
	for (int i = 2; i <= number; i++) {
		prime_list[i]=i;
	}

	for (int i = 2; i < sqrt(number); i++) {
		if (prime_list[i] == 0) 
			continue;
		for (int j = 2 * i; j <= number; j += i) //배수들을 제외
			prime_list[j] = 0;
	}
}

int main(void) {
	find_prime_list_under_number(20);
	for (int i = 0; i < 20; i++) {
		if (prime_list[i] == 0) 
			continue;
		cout << prime_list[i] << ' ';
	}
	return 0;
}