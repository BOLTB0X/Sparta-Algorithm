class Person:
    def __init__(self,param_name): #클래스 내부의 함수가 메소드
        print("i am created !",self)
        self.name = param_name
    
    def talk(self):
        print("안녕하세요, 제 이름은",self.name)

person_1=Person("유재석") #i am created ! <__main__.Person object at 0x000001F68802DFD0>
print(person_1.name) #유재석
person_1.talk() # 안녕하세요, 제 이름은 유재석

person_2=Person("방명수") #i am created ! <__main__.Person object at 0x000001F68802DEE0>
print(person_2.name) #방명수
person_2.talk() #안녕하세요, 제 이름은 방명수
