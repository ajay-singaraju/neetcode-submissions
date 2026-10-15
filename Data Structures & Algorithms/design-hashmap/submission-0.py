class MyHashMap:

    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:
        for el in self.data:
            if el[0] == key:
                el[1] = value
                return
        self.data.append([key, value])   

    def get(self, key: int) -> int:
        for el in self.data:
            if el[0] == key:
                return el[1]
        return -1

    def remove(self, key: int) -> None:
        for el in self.data:
            if el[0] == key:
                self.data.remove(el)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)