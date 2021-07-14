class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        # LinkedTuple
        # []
        # [(key, value)]
        self.items[index].add(key, value)

        # 만약, 입력된 key가 "fast" 인데 index 값이 2가 나왔다.
# 현재 self.items[2] 가 [("slow", "느린")] 이었다!
# 그렇다면 새로 넣는 key, value 값을 뒤에 붙여주자!
# self.items[2] == [("slow", "느린") -> ("fast", "빠른")] 이렇게! 

    def get(self, key):
        index = hash(key) % len(self.items)
        # LinkedTuple
        # [(key1, value1),(key2,value2)]
        return self.items[index].get(key)
