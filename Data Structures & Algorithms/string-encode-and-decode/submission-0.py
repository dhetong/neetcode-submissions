class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for itm in strs:
            encode_str = encode_str + itm + '<*>'
        return encode_str

    def decode(self, s: str) -> List[str]:
        decode_list = s.split('<*>')
        return decode_list[:len(decode_list)-1]
