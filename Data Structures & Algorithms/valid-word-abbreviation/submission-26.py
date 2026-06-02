class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i, j = 0, 0
        # abbr = 'imp4n5n' (i)
        # word = 'implementation' (j)
        length = ''
        while i < len(abbr) and j < len(word):
            if abbr[i].isdigit():
                if abbr[i] == '0':
                    return False
                while i < len(abbr) and abbr[i].isdigit(): # Found abbreviation
                    length += abbr[i]
                    i += 1
                j += int(length)

            else:
                if abbr[i] != word[j]:
                    return False
                length = ''
                i += 1
                j += 1
        return i == len(abbr) and j == len(word)
        
            
                

        