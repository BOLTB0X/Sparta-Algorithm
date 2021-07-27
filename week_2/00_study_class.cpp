#include <iostream>
#include <string>
using namespace std;

class Hello { //클래스
private: //내부에서만 사용
	string hello = "Hello Class";
public: //내부 외부 사용가능
	Hello(string h) {
		//기본 생성자 설정
		hello = h;
	}
	void show() {
		cout << hello << endl;
	}
};

void main(void) {
	//Hello a; //인스턴스를 사용할시 Hello class 출력
	Hello a = Hello("hihi");
	a.show();
} 
