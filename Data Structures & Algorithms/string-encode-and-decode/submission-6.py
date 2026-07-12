class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_list = []
        for itm in strs:
            length = len(itm)
            encode_itm = str(length) + '#' + itm
            encode_list.append(encode_itm)
        encode_str = "".join(encode_list)
        return encode_str

    def decode(self, s: str) -> List[str]:
        index_i = 0
        output = []
        while index_i < len(s):
            index_j = index_i + 1
            while s[index_j] != '#':
                index_j = index_j +1
            str_len = int(s[index_i:index_j])
            index_i = index_j + str_len + 1
            decode_str = s[index_j+1:index_i]
            output.append(decode_str)
        return output
