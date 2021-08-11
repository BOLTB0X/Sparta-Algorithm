#include<iostream>
#include<string>
using namespace std;

string st = "(())()";

bool is_correct_parenthesis(string str) {
	int check = 0;

	for (int i = 0; i < str.length(); i++) {
		if (check < 0)
			break;
		if (str[i] == '(')
			check++;
		else if (str[i] == ')')
			check--;
	}
	return check == 0 ? true : false;
}
int main(void) {
	bool ret=is_correct_parenthesis(st);

	cout << ret << '\n';
	return 0;
}