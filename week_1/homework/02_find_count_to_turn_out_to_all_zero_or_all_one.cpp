#include <iostream>
#include <string>
using namespace std;

int  find_count_to_turn_out_to_all_zero_or_all_one(string str) {
	int cnt_one_trans = 0; // 0 -> 1;
	int cnt_zero_trans = 0; // 1 -> 0;

	if (str[0] == '1')
		cnt_zero_trans += 1;
	else
		cnt_one_trans += 1;
	for (int i = 1; i < str.size(); i++) {
		if (str[i - 1] != str[i]) { // 앞 뒤 문자열이 다른 경우
			if (str[i] == '1')
				cnt_zero_trans += 1;
			else
				cnt_one_trans += 1;
		}
	}
	return min(cnt_one_trans,cnt_zero_trans);
}

int main(void) {
	cout << find_count_to_turn_out_to_all_zero_or_all_one("011110") << endl;
	return 0;
}