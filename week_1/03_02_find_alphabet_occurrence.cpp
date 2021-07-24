#include <iostream>
#include <string>
using namespace std;

char find_max_occurred_alphabet(string str) { //기존 알파벳별 빈도수 체크 배열이용 함수
	int alphabet_occurrence_array[26] = { 0, }; //알파벳별 빈도수를 저장하는 배열
	for (int i = 0; i < str.length(); i++) {
		if (!isalpha(str[i])) //해당 인덱스의 문자열에 알파벳이 아닌 경우
			continue;
		int arr_idx = (str[i] - 'a'); //아스키 코드 이용
		alphabet_occurrence_array[arr_idx] += 1;
	}
	int max_occurrence = 0; //최빈 변수
	int max_alphabet_idx = 0;
	
	for (int j = 0; j < 26; j++) { //알파벳 빈도수 최대 인덱스 찾기 위에서 사용한 배열 이용
		int alphabet_occurrence = alphabet_occurrence_array[j];
		if (max_occurrence < alphabet_occurrence) { // 크다면
			//교체 
			max_occurrence = alphabet_occurrence;
			max_alphabet_idx = j;
		}
	}
	return (max_alphabet_idx +'a'); //인덱스에 +'a'를 더하면 해당 알파벳으로 변환
}

int main(void) {
	cout << find_max_occurred_alphabet("Hello my name is sparta") << '\n';
	cout << find_max_occurred_alphabet("Sparta coding club") << '\n';
	cout << find_max_occurred_alphabet("best of best sparta") << '\n';
	return 0;
}
