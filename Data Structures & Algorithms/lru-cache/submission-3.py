class LRUCache:

    def __init__(self, capacity: int):
        self.key_list = []
        self.kvdict = defaultdict(int)
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.key_list:
            self.key_list.remove(key)
            self.key_list.append(key)
            return self.kvdict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.kvdict[key] = value
        if key in self.key_list:
            self.key_list.remove(key)
            self.key_list.append(key)
        else:
            self.key_list.append(key)
        if len(self.key_list) > self.cap:
            remove_key = self.key_list.pop(0)
            self.kvdict.pop(remove_key)
