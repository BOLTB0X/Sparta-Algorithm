#include <iostream>
#include <string>
using namespace std;

char find_max_occurred_alphabet(string str) {
	int alphabet_occurrence_array[26] = { 0, }; //알파벳별 빈도수를 저장하는 배열
	for (int i = 0; i < str.length(); i++) {
		if (!isalpha(str[i]))
			continue;
		int arr_idx = (str[i] - 'a');
		alphabet_occurrence_array[arr_idx] += 1;
	}
	int max_occurrence = 0; //최빈 변수
	int max_alphabet_idx = 0;
	
	for (int j = 0; j < 26; j++) { //알파벳 빈도수 최대 인덱스 찾기
		int alphabet_occurrence = alphabet_occurrence_array[j];
		if (max_occurrence < alphabet_occurrence) {
			max_occurrence = alphabet_occurrence;
			max_alphabet_idx = j;
		}
	}
	return (max_alphabet_idx +'a');
}

int main(void) {
	cout << find_max_occurred_alphabet("Hello my name is sparta") << '\n';
	cout << find_max_occurred_alphabet("Sparta coding club") << '\n';
	cout << find_max_occurred_alphabet("best of best sparta") << '\n';
	return 0;
}