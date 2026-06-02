class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s))
            encoded += '#'
            encoded += s

        return encoded

        # return self.decode(encoded)

    def decode(self, encoded):
        strs = []
        i = 0

        while i < len(encoded):
            
            j = i
            while encoded[j] != '#':
                j += 1

            length = int(encoded[i:j])
            strs.append(encoded[j + 1 : j + 1 + length])
            i = j + 1 + length

        return strs
            

