#include <iostream>
#include <string>
using namespace std;

char find_max_occurred_alphabet(string str) {
	int alphabet_occurrence_array[26] = { 0, }; //���ĺ��� �󵵼��� �����ϴ� �迭
	for (int i = 0; i < str.length(); i++) {
		if (!isalpha(str[i]))
			continue;
		int arr_idx = (str[i] - 'a');
		alphabet_occurrence_array[arr_idx] += 1;
	}
	int max_occurrence = 0; //�ֺ� ����
	int max_alphabet_idx = 0;
	
	for (int j = 0; j < 26; j++) { //���ĺ� �󵵼� �ִ� �ε��� ã��
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