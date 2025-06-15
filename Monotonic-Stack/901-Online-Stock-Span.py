class StockSpanner_failed_attempt:

    def __init__(self):
        self.quotes = [] # Store everyday's price 

    def next(self, price: int) -> int:
        # Update latest price records
        self.quotes.append(price)
        if len(self.quotes) == 1:
            return 1
        stack = []
        last_high_price_day = 0
        # Find the last price that's higher than today's price
        for index, p in enumerate(self.quotes):
            # Build stack to track 
            while stack and p < self.quotes[stack[-1]]:
                last_high_price_day = stack.pop()
            
            stack.append(index)

        span = stack[-1] - last_high_price_day
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

'''
### Wrong Answer ###

Inptut
["StockSpanner","next","next","next","next","next","next","next"]
[[],[100],[80],[60],[70],[60],[75],[85]]

Output
[null,1,1,1,2,1,2,3]

Expected
[null,1,1,1,2,1,4,6]
'''

class StockSpanner:

    def __init__(self):
        self.stack = [] # Store (price, index) pairs
        self.index_pointer = 0 # Tracks the current day

    def next(self, price: int) -> int:
        # Pop elements from stack while current price is greater or equal
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        
        # Compute span
        if self.stack:
            last_high_price_day = self.stack[-1][1]
        else:
            last_high_price_day = -1 # No previous day with a higher price

        span = self.index_pointer - last_high_price_day

        # Update price records
        self.stack.append((price, self.index_pointer))

        self.index_pointer += 1 # Move to the next day
        
        return span
