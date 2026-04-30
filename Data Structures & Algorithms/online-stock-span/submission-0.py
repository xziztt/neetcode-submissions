class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 0
        self.stack.append(price)
        currStack = self.stack.copy()
        while currStack and price >= currStack[-1]:
            span += 1
            currStack.pop()


        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)