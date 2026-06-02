class Solution:

    def encode(self, strs: List[str]) -> str:
        combined = ''
        lengths = ''
        for s in strs:
            combined += s
            lengths += str(len(s)) + ','
        return combined + lengths + str(len(lengths))


    def decode(self, s: str) -> List[str]:
        if (s == '0'):
            return []

        i = 0
        while s[i] != ',':
            i-=1

        len_lens = int(s[i+1:])
        str_lens = s[-len_lens+i+1: i]
        str_lens = str_lens.split(',')
        print(str_lens)

        strs = []
        start = 0

        for length in str_lens:
            length = int(length)
            strs.append(s[start: start+length])
            start += length

        return strs
