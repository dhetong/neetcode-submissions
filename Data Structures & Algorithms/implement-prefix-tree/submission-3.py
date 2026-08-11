class PrefixTree:

    def __init__(self):
        self.dict = dict()

    def insert(self, word: str) -> None:
        tmp_dict = self.dict
        for c in list(word[:len(word)-1]):
            if c in tmp_dict:
                tmp_dict, flag = tmp_dict[c]
            else:
                tmp_dict[c] = (dict(), False)
                tmp_dict = tmp_dict[c][0]
        c = list(word)[-1]
        if c in tmp_dict:
            new_tmp_dict, flag = tmp_dict[c]
            tmp_dict[c] = (new_tmp_dict, True)
        else:
            tmp_dict[c] = (dict(), True)                 

    def search(self, word: str) -> bool:
        tmp_dict = self.dict
        flag = False
        for c in list(word):
            if c in tmp_dict:
                tmp_dict, flag = tmp_dict[c]
            else:
                return False
        print(word)
        print(flag)
        if flag == False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        tmp_dict = self.dict
        for c in list(prefix):
            if c in tmp_dict:
                tmp_dict, flag = tmp_dict[c]
            else:
                return False
        return True        