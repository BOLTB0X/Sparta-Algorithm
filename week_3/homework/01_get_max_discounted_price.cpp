#include <iostream>
#include <algorithm>
#include <array>
using namespace std;
int shop_prices[] = { 30000, 2000, 1500000 };
int user_coupon[] = { 20,40 };

bool compare(int i, int j) {
	return j < i;
}

int get_max_discounted_price() {
	int max_value = 0;
	int p_size = sizeof shop_prices / sizeof 0;
	int c_size = sizeof user_coupon / sizeof 0;

	sort(shop_prices, shop_prices + p_size, compare);
	sort(user_coupon, user_coupon + c_size, compare);
	int idx = 0;
	for (int j = 0; j < c_size; j++) {
		int discount=(int)(((100 - user_coupon[j]) * 0.01)* shop_prices[j]);
		max_value += discount;
		idx += 1;
	}
	for (int i = idx; i < p_size; i++) {
		max_value += shop_prices[i];
	}

	return max_value;
}

int main(void) {
	

	cout << get_max_discounted_price() << '\n';
	return 0;
}