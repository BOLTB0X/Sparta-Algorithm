#include <iostream>
#include <string>
using namespace std;

int alphabet_occurrence_array[26] = { 0, }; //알파벳별 빈도수를 저장하는 배열

int* find_alphabet_occurrence_array(int *alphabet_occurrence_array,string str) {
	
	for (int i = 0; i < str.length(); i++) {
		if (!isalpha(str[i]))
			continue;
		int arr_idx = str[i] - 'a'; //아스키코드를 이용
		alphabet_occurrence_array[arr_idx] += 1; //해당 아스키코드값에 해당하는 인덱스로 빈도수를 카운트
	}

	return alphabet_occurrence_array;
}

int main(void) {
	string str;
	int* answer=find_alphabet_occurrence_array(alphabet_occurrence_array,"Hello my name is sparta");

	for (int i = 0; i < 26; i++) {
		cout << answer[i] << ' ';
	}
	cout << endl;
	return 0;
}
