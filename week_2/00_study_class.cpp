#include <iostream>
#include <string>
using namespace std;

class Hello { //Ŭ����
private: //���ο����� ���
	string hello = "Hello Class";
public: //���� �ܺ� ��밡��
	Hello(string h) {
		//�⺻ ������ ����
		hello = h;
	}
	void show() {
		cout << hello << endl;
	}
};

void main(void) {
	//Hello a; //�ν��Ͻ��� ����ҽ� Hello class ���
	Hello a = Hello("hihi");
	a.show();
}