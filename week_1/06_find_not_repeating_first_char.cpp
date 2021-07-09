#include <iostream>
#include <string>
#include <vector>
using namespace std;

char find_not_repeating_first_character(string str) {
	int alphabet_occurrence_array[26] = { 0, }; //알파벳별 빈도수를 저장하는 배열
	for (int i = 0; i < str.length(); i++) {
		if (!isalpha(str[i]))
			continue;
		int arr_idx = str[i] - 'a';
		alphabet_occurrence_array[arr_idx] += 1;
	}
	vector<char> not_repeating_character_array;

	for (int i = 0; i < 26; i++) {
		int alphabet_occurrence = alphabet_occurrence_array[i];

		if (alphabet_occurrence == 1)
			not_repeating_character_array.push_back(i + 'a');
	}

	for (int i = 0; i < str.length(); i++) {
		for (int j = 0; j < not_repeating_character_array.size(); j++) {
			if (str[i] == not_repeating_character_array[j])
				return not_repeating_character_array[j];
		}
	}
	return '-';
}
int main(void) {

	cout << find_not_repeating_first_character("abadabac") << '\n';
	cout << find_not_repeating_first_character("aabbcddd") << '\n';
	cout << find_not_repeating_first_character("aaaaaaaaaaaa") << '\n';
	return 0;
}
