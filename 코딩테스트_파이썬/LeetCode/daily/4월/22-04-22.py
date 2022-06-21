class MyHashMap:

    def __init__(self):
        self.myMap = dict()

    def put(self, key: int, value: int) -> None:
        self.myMap[key] = value

    def get(self, key: int) -> int:
        if key in self.myMap:
            return self.myMap[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.myMap:
            del (self.myMap[key])
