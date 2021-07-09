#include <iostream>
#include <string>
using namespace std;
char alphabet_array[26] = { 'a', 'b', 'c', 'd', 'e', 'f','g' , 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
't', 'u', 'v', 'x', 'y', 'z'};

char find_max_occurred_alphabe(string str) {
	int max_occurrence = 0; //최빈 변수
	char max_alphabet = alphabet_array[0];

	for (int i = 0; i < 26; i++) {
		int occurrence = 0;
		for (int j = 0; j < str.length(); j++) { //입력받은 str의 알파벳 빈도수 체크
			if (alphabet_array[i] == str[j]) occurrence += 1;
		}
		if (max_occurrence < occurrence) {
			max_occurrence = occurrence;
			max_alphabet = alphabet_array[i];
		}
	}
	return max_alphabet;
}

int main(void) {
	char answer = find_max_occurred_alphabe("Hello my name is sparta");
	cout << answer << '\n';
	answer= find_max_occurred_alphabe("Sparta coding club");
	cout << answer << '\n';
	answer = find_max_occurred_alphabe("best of best sparta");
	cout << answer << '\n';
	return 0;
}