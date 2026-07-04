class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = len(prices)
        min_buy_price = prices[0]
        max_profit = 0
        for i in range(1, L):
            if prices[i] < min_buy_price:
                min_buy_price = prices[i]
            else:
                profit = prices[i] - min_buy_price
                if (profit > max_profit):
                    max_profit = profit
        return max_profit


if __name__ == '__main__':
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))