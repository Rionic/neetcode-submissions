class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += '#' + str(len(s)) + '#' + s
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                if i < len(s) - 1 and s[i + 1] != '#': # start counting numbers
                    i += 1
                    length = ''
                    while s[i].isdigit():
                        length += s[i]
                        i += 1
                    i += 1 # skip the ending hash
                    if length == '':
                        length = 0
                    else:
                        length = int(length)
                decoded.append(s[i: i + length])
                i += length
            else:
                i += 1
        print(decoded)
        return decoded






