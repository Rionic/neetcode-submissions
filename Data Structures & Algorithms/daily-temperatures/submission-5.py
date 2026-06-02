class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while s and t > temperatures[s[-1]]:
                print(t, temperatures[s[-1]])
                s_i = s.pop()
                res[s_i] = i - s_i # we found a greater temp. update prev day
                print('res', res)
            print('append', i)
            s.append(i)
        return res

        # [30,38,30,36,35,40,28]
        #                     ^  
        # s = [5, 6] 
        # o = [1, 4, 1, 2, 1, 0, 0]  