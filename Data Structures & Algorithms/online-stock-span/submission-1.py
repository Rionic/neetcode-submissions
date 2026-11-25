class StockSpanner:

    def __init__(self):
        self.s = []
        

    def next(self, price: int) -> int:
        # Stack holds (price, span)
        # prices = [5,4,3,2,4]
        # s = [(5,1),(4,1),(3,1),(2,1),(4,4)] 
        # on (4,4), pop all <= price of 4! this (4,4) basically holds
        # the answer for everything after (5,1) -> s = [(5,1), (4,4)]
        span = 1
        while self.s and self.s[-1][0] <= price:
            span += self.s.pop()[1]

        self.s.append((price, span))        

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)